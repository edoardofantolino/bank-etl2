from extract import extract
from transform import transform
from load import load
from logger import get_logger
from pathlib import Path
import uuid
import pandas as pd
from datetime import datetime

ingestion_timestamp = datetime.utcnow()

pipeline_run_id = str(uuid.uuid4())

log = get_logger()
log.info("ETL START")

# 1. Extract
df = extract("../data/raw/transactions.csv")
log.info(f"Extracted rows: {len(df)}")

# 2. Transform
df_valid, df_invalid, df_rejected = transform(df, pipeline_run_id)

log.info(f"Valid rows: {len(df_valid)}")
log.info(f"Invalid rows: {len(df_invalid)}")

# creation of etl_run info table
df_run = pd.DataFrame({
    "pipeline_run_id": [pipeline_run_id],
    "raw_rows": [len(df)],
    "valid_rows": [len(df_valid)],
    "rejected_rows": [df_rejected["transaction_id"].nunique()],
    "execution_timestamp": [ingestion_timestamp]
})

# 3. Load
load(df_valid, df_rejected, df_run, "../bank.db")

df_valid.to_csv("../data/output/valid_transactions.csv", index=False)
df_rejected.to_csv("../data/output/rejected_transactions_reasons.csv", index=False)
df_run.to_csv(
    "../data/output/etl_runs.csv",
    mode="a",
    header=not Path("../data/output/etl_runs.csv").exists(),
    index=False
)


log.info("Load completed")
log.info("ETL END")