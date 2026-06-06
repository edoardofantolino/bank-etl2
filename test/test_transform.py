from src.transform import clean_date
from src.transform import clean_amount
import pandas as pd

data = [
        {"transaction_id": 1, "date": "17/04/2026", "account": "IT2345", "amount": 2940.96, "currency": "EUR", "type": "deposit"},
        {"transaction_id": 2, "date": "17/05/2025", "account": "IT2345", "amount": 4462.88, "currency": "EUR", "type": "deposit"},
        {"transaction_id": 3, "date": "10/05/2026", "account": "IT4567", "amount": 877.56, "currency": "EUR", "type": "transfer"},
        {"transaction_id": 4, "date": "20/03/2026", "account": "IT7890", "amount": -975.96, "currency": "EUR", "type": "withdrawal"}
    ]


# Verify if the clean_date function do not leave nan values
def test_clean_date():

    df = pd.DataFrame(data)

    df = clean_date(df)

    print(df["date"].isna().any())

    assert df["date"].notna().all()


# Verify if the clean_amount function do not leave nan values
def test_clean_amount():

    df = pd.DataFrame(data)
    
    print(df)

    df = clean_amount(df)
    print(df["amount"].isna().any())

    print(df)

    assert not df["amount"].isna().any()


# Verify that transaction id is unique
def test_transaction_id_unique():
    df = pd.DataFrame(data)
    df = clean_date(df)

    assert df["transaction_id"].is_unique