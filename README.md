# 用 Python 理財：打造加密貨幣實戰策略｜課程教材

[![weekly](https://github.com/finlab-python/hahow-crypto-course/actions/workflows/weekly.yml/badge.svg)](https://github.com/finlab-python/hahow-crypto-course/actions/workflows/weekly.yml)

Hahow 課程 [用 Python 理財：打造加密貨幣實戰策略](https://hahow.in/cr/crypto-python) 的官方程式教材（2026 年更新版）。

- 打開就能跑：在 Google Colab 按一下就能執行，不需要安裝 Docker，也不需要幣安帳號或 API 金鑰。
- 每個有程式的單元都有對應的筆記本，筆記本開頭寫著「對應影片」與「和影片的差異」。
- 每週自動在 GitHub（美國主機）把所有筆記本從頭跑到尾，確認教材一直能用。

## 一分鐘開始

1. 在下方對照表點選單元的 **Colab** 連結（需要登入 Google 帳號）。
2. 從第一格開始依序執行（`Shift + Enter`）。第一格會安裝課程套件 `finlab_crypto`，約需 1 分鐘。
3. 看到 `Warning: This notebook was not authored by Google` 時選「仍要執行」。

想保存自己的修改：Colab 選單「檔案 → 在雲端硬碟中儲存複本」。

## 單元對照表

| 章 | 單元 | 筆記本 | Colab |
|---|---|---|---|
| 1 | 1-1 ~ 1-5 為什麼要投資加密貨幣、量化交易 | （觀念講解，沒有程式） | |
| 2 | 2-1 ~ 2-4、作業 2-A1 ~ 2-A3 購買、轉帳、簡易投資 | （交易所實務，沒有程式） | |
| 3 | 3-1 如何搭建 Python 雲端平台 | 請看 [3-2](3-2_python_basics.ipynb) 的 Colab 連結，第一次開啟就是在練習 3-1 的內容 | |
| 3 | 3-2 Python 快速入門 | [3-2_python_basics.ipynb](3-2_python_basics.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/3-2_python_basics.ipynb) |
| 3 | 3-3 Pandas 快速入門 | [3-3_pandas_basics.ipynb](3-3_pandas_basics.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/3-3_pandas_basics.ipynb) |
| 3 | 作業 3-A1 加密貨幣價格分析 | [起始](3-A1_price_analysis.ipynb)、[解答](3-A1_price_analysis_solution.ipynb) | [起始](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/3-A1_price_analysis.ipynb)、[解答](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/3-A1_price_analysis_solution.ipynb) |
| 4 | 4-1 ~ 4-7 雲端回測平台 I ~ VII（下載數據、買賣訊號、回測、模組化、最佳化、過擬合原理／圖表）＋停損停利補充 | [4-1_backtest_platform.ipynb](4-1_backtest_platform.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/4-1_backtest_platform.ipynb) |
| 4 | 作業 4-A1 自行研發策略 | [4-A1_own_strategy.ipynb](4-A1_own_strategy.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/4-A1_own_strategy.ipynb) |
| 5 | 5-1 ~ 5-4 趨勢策略研發、8 種趨勢策略、最佳化、驗證 | [5-2_trend_strategies.ipynb](5-2_trend_strategies.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/5-2_trend_strategies.ipynb) |
| 5 | 5-5 MMI 濾網、5-6 Filter 打包 | [5-5_mmi_filter.ipynb](5-5_mmi_filter.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/5-5_mmi_filter.ipynb) |
| 5 | 作業 5-A1 Market Meanness Index | [5-A1_mmi_filter.ipynb](5-A1_mmi_filter.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/5-A1_mmi_filter.ipynb) |
| 5 | 5-7、5-8 Talib Strategy Builder 1、2 | [5-7_talib_strategy_builder.ipynb](5-7_talib_strategy_builder.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/5-7_talib_strategy_builder.ipynb) |
| 5 | 作業 5-A2 Talib Strategy Builder | [5-A2_talib_strategy_builder.ipynb](5-A2_talib_strategy_builder.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/5-A2_talib_strategy_builder.ipynb) |
| 6 | 6-1 Bitcoin Hash Rate | [6-1_hash_rate.ipynb](6-1_hash_rate.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/6-1_hash_rate.ipynb) |
| 6 | 6-2 Puell Multiple | [6-2_puell_multiple.ipynb](6-2_puell_multiple.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/6-2_puell_multiple.ipynb) |
| 6 | 作業 6-A1 用 Puell Multiple 設計存幣方式 | [6-A1_puell_multiple.ipynb](6-A1_puell_multiple.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/6-A1_puell_multiple.ipynb) |
| 6 | 6-3 SOPR | [6-3_sopr.ipynb](6-3_sopr.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/6-3_sopr.ipynb) |
| 6 | 作業 6-A2 交易所出入金策略研發 | [6-A2_exchange_flows.ipynb](6-A2_exchange_flows.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/6-A2_exchange_flows.ipynb) |
| 7 | 7-1 風險報酬模型、7-2 HRP、7-3 Walk forward 資產配置 | [7-2_hrp_walk_forward.ipynb](7-2_hrp_walk_forward.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/7-2_hrp_walk_forward.ipynb) |
| 7 | 7-4 Multi-asset Strategies | [7-4_multi_asset_strategies.ipynb](7-4_multi_asset_strategies.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/7-4_multi_asset_strategies.ipynb) |
| 7 | 作業 7-A1 建立自己的投資系統 | [7-A1_own_portfolio.ipynb](7-A1_own_portfolio.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/7-A1_own_portfolio.ipynb) |
| 8 | 8-1 策略監控、8-2 / 8-3 資產配置系統、8-4 串接 Binance API 自動下單 | [8-1_trading_portfolio.ipynb](8-1_trading_portfolio.ipynb) | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/8-1_trading_portfolio.ipynb) |
| 8 | 8-5 Google Cloud Function、8-6 Cloud Scheduler | [8-5_cloud_function.ipynb](8-5_cloud_function.ipynb)＋[cloud_function/](cloud_function/)（部署範例） | [Colab](https://colab.research.google.com/github/finlab-python/hahow-crypto-course/blob/main/8-5_cloud_function.ipynb) |
| 8 | 作業 8-A1 建立自己的雲端自動化系統 | 以 [cloud_function/](cloud_function/) 為起點，修改 `main.py` 的策略 | |
| 8 | 8-7 總結 | （沒有程式） | |

## 在自己的電腦執行

需要 Python 3.11 ~ 3.13（Windows、macOS、Linux 皆可）。

```bash
git clone https://github.com/finlab-python/hahow-crypto-course.git
cd hahow-crypto-course
python -m venv .venv
source .venv/bin/activate        # Windows：.venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

TA-Lib 已經有官方安裝檔（wheel），不需要另外安裝 C 函式庫；也不再需要 Docker。
VS Code 使用者可以直接開啟 `.ipynb`，選擇 `.venv` 當作 kernel。

## 和影片的差異（總覽）

各筆記本開頭都有該單元的詳細差異，這裡列出影響最大的幾項：

- **資料來源**：K 線改從幣安公開資料端點 `data-api.binance.vision` 下載，不需要金鑰、在 Colab 也能用。
  `finlab_crypto.crawler.get_all_binance('BTCUSDT', '4h')` 的寫法和影片完全一樣。
- **不再需要 Docker**，也不需要 `pip install talib-binary`；第一格 `%pip install -q finlab_crypto==0.3.0` 就裝好所有東西。
- **`finlab_crypto.setup()`** 只建立 `history/` 暫存資料夾，不會再要求連結 Google Drive。
- **鏈上資料**：Glassnode 已經沒有免費 API。算力、交易所流入流出改用 Coin Metrics 社群版，SOPR 改用 BGeometrics，都不需要金鑰。
- **vectorbt 新版**：`cumulative_returns()`、`final_value()`、`daily_returns()` 都要加括號。
- **資料變多了**：1 小時 K 線從錄影時約 2.8 萬根成長到 8 萬根以上；最佳化較重的單元預設只用近幾年資料（筆記本裡的 `START`），
  讓 Colab 免費版幾分鐘內跑完。最佳參數與績效數字會和影片不同，這是正常的。
- **下架的幣種**：VETBTC 已於 2026 年 3 月下架，改用 BNBBTC。

## 常見問題

### 為什麼舊版的 Colab 筆記本不能用了？

有三個原因，新版教材都已經解決：

1. **幣安的地區限制**：`api.binance.com` 會對美國 IP 回覆 HTTP 451（Service unavailable from a restricted location）。
   Colab 的主機在美國，舊版套件在 `import finlab_crypto` 時就會連線 `api.binance.com`，所以第一行就失敗。
   新版改用幣安官方的公開市場資料端點 `data-api.binance.vision`，美國主機也能下載（每週的自動測試就是在美國主機上跑）。
2. **套件太舊**：Colab 已升級到 Python 3.13、numpy 2、pandas 2，舊版依賴（例如 `talib-binary` 只支援到 Python 3.7）裝不起來。
3. **Glassnode 改為付費**：第 6 章原本用的免費 API 已經停止。

### Colab 上可以自動下單嗎？

不行，也不建議。下單一定要連 `api.binance.com`，Colab 在美國會被拒絕（HTTP 451）。
在 Colab 上請用 dry run（不設定 API 金鑰）確認訊號與訂單；真正下單請在自己的電腦執行，
或部署到台灣區域（asia-east1）的 Cloud Function，步驟見 [cloud_function/README.md](cloud_function/README.md)。

### 我的 Colab 跑很久或記憶體不足？

- 參數最佳化會同時回測上千組參數，較重的單元可能要幾分鐘。
- 筆記本裡的 `START` 決定最佳化用哪一天之後的資料；改成更晚的日期會更快。
- Colab 閒置一段時間會重置，`history/` 裡的暫存資料會消失，重新執行時會自動重新下載。

### API 金鑰要怎麼保管？

- 在幣安建立 API 金鑰時只勾選「現貨交易」，**不要開啟提現權限**，並設定 IP 白名單。
- 金鑰不要寫進筆記本或程式碼（分享、上傳 GitHub 就外洩了）。本機執行時用環境變數：

  ```bash
  export BINANCE_KEY=你的金鑰
  export BINANCE_SECRET=你的密鑰
  jupyter lab
  ```

  Windows PowerShell：`$env:BINANCE_KEY="你的金鑰"`。部署到雲端時放在 Secret Manager。
- 金鑰外洩時，立刻到幣安「API 管理」刪除該金鑰。

### SOPR 下載失敗？

SOPR 的免費資料源每個 IP 每小時約可下載 10 次，`finlab_crypto` 會把資料暫存 12 小時；
短時間內重複下載被拒絕時，稍等一小時再試即可。

### 出現錯誤該怎麼辦？

先確認第一格安裝有執行、而且是從第一格依序執行。仍有問題請到 Hahow 課程的問答區發問，附上錯誤訊息的截圖。

## 自動測試

[`.github/workflows/weekly.yml`](.github/workflows/weekly.yml) 每週一在 GitHub 的美國主機上：

1. 執行 `finlab_crypto` 套件的測試
2. 以 `QUICK_RUN=True`（縮小最佳化範圍）把每一本筆記本從頭跑到尾

也可以在 Actions 頁面手動觸發。

## 資料來源

- K 線、交易對資訊：幣安公開市場資料（`data-api.binance.vision`）
- 算力、發行量、交易所流入流出：[Coin Metrics Community Data](https://coinmetrics.io/community-network-data/)（CC BY-NC 4.0）
- SOPR：[BGeometrics](https://bitcoin-data.com)
- 股票、ETF 與指數（第 7 章）：Yahoo Finance（yfinance）

公開分享研究結果時請註明資料來源。
