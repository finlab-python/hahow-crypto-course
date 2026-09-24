# 8-5、8-6 Cloud Function 自動交易（部署範例）

對應影片：第 8 章 單元 8-5【雲端自動化】用 Google Cloud Function 建構自動交易介面、8-6【雲端自動化】用 Cloud Scheduler 做排程

| 檔案 | 用途 |
|---|---|
| `main.py` | HTTP 進入點 `main`：計算訊號與訂單、下單、回傳 HTML 報表 |
| `requirements.txt` | 雲端安裝的套件（固定 `finlab_crypto` 版本） |

先在 [8-5 筆記本](../8-5_cloud_function.ipynb) 用 dry run 確認策略與報表，再照下面的步驟部署。

## 和影片的差異

- 影片在 Cloud Console 網頁上貼程式；這裡改用 `gcloud` 指令，步驟可以複製貼上，也不會漏設定。
- 使用第 2 代 Cloud Functions（Cloud Run functions）、Python 3.12，區域 `asia-east1`（台灣）：
  幣安會拒絕美國 IP（HTTP 451），函式必須部署在美國以外的區域。
- API 金鑰放在 Secret Manager，不寫進程式碼。
- 函式**不公開**（`--no-allow-unauthenticated`），只有 Cloud Scheduler 的服務帳戶能呼叫；
  影片中公開網址 + `?mode=MARKET` 的做法，任何知道網址的人都能替你下單。

## 部署

需要：已啟用帳單的 GCP 專案、安裝 [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)。

```bash
PROJECT_ID=your-project-id
REGION=asia-east1
gcloud config set project $PROJECT_ID
gcloud services enable cloudfunctions.googleapis.com run.googleapis.com cloudbuild.googleapis.com \
    artifactregistry.googleapis.com secretmanager.googleapis.com cloudscheduler.googleapis.com

# 1. 把幣安 API 金鑰存進 Secret Manager（執行後貼上金鑰，按 Ctrl-D 結束）
gcloud secrets create binance-key --data-file=-
gcloud secrets create binance-secret --data-file=-

# 2. 允許函式的執行身分讀取金鑰（第 2 代函式預設使用 Compute Engine 預設服務帳戶）
RUNTIME_SA=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')-compute@developer.gserviceaccount.com
for SECRET in binance-key binance-secret; do
  gcloud secrets add-iam-policy-binding $SECRET \
      --member=serviceAccount:$RUNTIME_SA --role=roles/secretmanager.secretAccessor
done

# 3. 部署（在本資料夾內執行）
gcloud functions deploy crypto-rebalance \
    --gen2 --runtime=python312 --region=$REGION \
    --source=. --entry-point=main --trigger-http --no-allow-unauthenticated \
    --memory=1Gi --timeout=300s \
    --set-env-vars=NUMBA_CACHE_DIR=/tmp \
    --set-secrets=BINANCE_KEY=binance-key:latest,BINANCE_SECRET=binance-secret:latest
```

手動呼叫一次（預設 `TEST`，不會成交），確認報表：

```bash
URL=$(gcloud functions describe crypto-rebalance --gen2 --region=$REGION --format='value(serviceConfig.uri)')
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" "$URL?mode=TEST" > report.html
```

## 8-6 用 Cloud Scheduler 排程

4 小時 K 線在 UTC 0、4、8、12、16、20 點收盤；排在收盤後 1 分鐘執行。
[crontab.guru](https://crontab.guru/) 可以幫你檢查 cron 語法。

```bash
# 建立排程專用的服務帳戶，並只給它呼叫這個函式的權限
gcloud iam service-accounts create crypto-scheduler
SCHEDULER_SA=crypto-scheduler@$PROJECT_ID.iam.gserviceaccount.com
gcloud functions add-invoker-policy-binding crypto-rebalance \
    --region=$REGION --member=serviceAccount:$SCHEDULER_SA

gcloud scheduler jobs create http crypto-rebalance-4h \
    --location=$REGION --schedule="1 */4 * * *" --time-zone="Etc/UTC" \
    --uri="$URL" --http-method=POST \
    --headers=Content-Type=application/json --message-body='{"mode": "TEST"}' \
    --oidc-service-account-email=$SCHEDULER_SA
```

確認 `TEST` 模式的報表都正確之後，再把 `--message-body` 改成 `{"mode": "LIMIT"}`：

```bash
gcloud scheduler jobs update http crypto-rebalance-4h --location=$REGION --message-body='{"mode": "LIMIT"}'
```

## 費用與關閉

每 4 小時執行一次，一個月約 180 次，在 Cloud Functions、Cloud Scheduler（每個帳戶 3 個免費排程）的免費額度內；
Secret Manager 與映像檔儲存每月約幾美分。詳見 [Cloud Run functions 定價](https://cloud.google.com/functions/pricing)。

不用時刪除：

```bash
gcloud scheduler jobs delete crypto-rebalance-4h --location=$REGION
gcloud functions delete crypto-rebalance --gen2 --region=$REGION
```
