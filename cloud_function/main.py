"""Cloud Function: rebalance a Binance spot account with the course strategies.

HTTP entry point ``main``: ``?mode=TEST|LIMIT|MARKET`` or JSON body ``{"mode": ...}``.
API keys come from the environment (Secret Manager), never from the source.
"""
import os

import functions_framework

from finlab_crypto.indicators import trends
from finlab_crypto.online import TradingMethod, TradingPortfolio, render_html
from finlab_crypto.strategy import Strategy

DEFAULT_MODE = 'TEST'
MARGIN_USDT = 1000


@Strategy(name='sma', n1=20, n2=40)
def trend_strategy(ohlcv):
    fast = trends[trend_strategy.name](ohlcv.close, trend_strategy.n1)
    slow = trends[trend_strategy.name](ohlcv.close, trend_strategy.n2)
    entries = (fast > slow) & (fast.shift() < slow.shift())
    exits = (fast < slow) & (fast.shift() > slow.shift())
    return entries, exits, {'overlaps': {'trend1': fast, 'trend2': slow}}


TRADING_METHODS = [
    TradingMethod(
        symbols=['XRPBTC', 'ADABTC', 'LINKBTC', 'ETHBTC', 'BNBBTC'],
        freq='4h',
        lookback=1000,
        strategy=trend_strategy,
        variables={'name': 'sma', 'n1': 30, 'n2': 130},
        weight_btc=0.01,
        name='altcoin-trend-sma',
    ),
    TradingMethod(
        symbols=['BTCUSDT'],
        freq='4h',
        lookback=1000,
        strategy=trend_strategy,
        variables={'name': 'hullma', 'n1': 70, 'n2': 108},
        weight_btc=0.05,
        name='btc-trend-hullma',
    ),
]


def rebalance(mode):
    """Compute signals, target positions and orders, place them, and return an HTML report."""
    tp = TradingPortfolio(os.environ.get('BINANCE_KEY'), os.environ.get('BINANCE_SECRET'))
    for method in TRADING_METHODS:
        tp.register(method)
    tp.register_margin('USDT', MARGIN_USDT)

    ohlcvs = tp.get_ohlcvs()
    signals = tp.get_latest_signals(ohlcvs)
    position, position_btc, orders = tp.calculate_position_size(signals)
    order_results = tp.execute_orders(orders, mode=mode)
    return render_html(signals, position, position_btc, orders, order_results)


@functions_framework.http
def main(request):
    body = request.get_json(silent=True) or {}
    mode = request.args.get('mode') or body.get('mode') or DEFAULT_MODE
    return rebalance(mode)
