import pandas as pd
from datetime import datetime

ingestion_timestamp = datetime.utcnow()

# TEST function for CI
def add(a, b):
    return a + b

def clean_date(df):
    ## DATA MANAGEMENT

    df["date"] = (
        df["date"]
        .str.replace("/", "-")
        .str.strip()
    )

    df["date"] = df["date"].str.replace(
        r"(\d{4})-(\d{2})-(\d{2})",
        r"\3-\2-\1",
        regex=True
    )

    # 1. Parse dates
    df["date"] = pd.to_datetime(
        df["date"],
        dayfirst=True,
        errors="coerce"
    )

    return df


def transform(df, pipeline_run_id):
    
    df = clean_date(df)

    ## AMOUNT MANAGEMENT
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Add rejection reason
    df["rejection_reasons"] = ""

    df.loc[df["date"].isna(), "rejection_reasons"] += "invalid_date,"
    df.loc[df["amount"].isna(), "rejection_reasons"] += "invalid_amount,"

    df["rejection_reasons"] = df["rejection_reasons"].str.strip(",")
    df["rejection_reasons"] = df["rejection_reasons"].apply(
        lambda x: x.split(",") if x else []
    )

    df_valid = df[df["rejection_reasons"].str.len() == 0]
    df_invalid = df[df["rejection_reasons"].str.len() > 0]

    df_valid = df_valid.drop(columns=["rejection_reasons"])
    df_valid["pipeline_run_id"] = pipeline_run_id
    df_valid["ingestion_timestamp"] = ingestion_timestamp

    # EXPLODE INTO ROWS
    df_rejected = df_invalid.copy()
    df_rejected = df_rejected.explode("rejection_reasons")

    # RENAME COLUMN
    df_rejected = df_rejected.rename(columns={
        "rejection_reasons": "reason"
    })

    # REMOVE REDUNDANT COLUMNS
    df_rejected = df_rejected[["transaction_id", "reason"]]
    df_rejected["pipeline_run_id"] = pipeline_run_id
    df_rejected["ingestion_timestamp"] = ingestion_timestamp

    return df_valid, df_invalid, df_rejected