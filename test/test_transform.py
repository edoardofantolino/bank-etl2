from src.transform import clean_date
from src.transform import add
import pandas as pd

def test_clean_date():
    data = [
        {"transaction_id": 1, "date": "17/04/2026", "account": "IT2345", "amount": 2940.96, "currency": "EUR", "type": "deposit"},
        {"transaction_id": 2, "date": "02/02/2026", "account": "IT2345", "amount": 4462.88, "currency": "EUR", "type": "deposit"},
        {"transaction_id": 3, "date": "10/05/2026", "account": "IT4567", "amount": 877.56, "currency": "EUR", "type": "transfer"},
        {"transaction_id": 4, "date": "20/03/2026", "account": "IT7890", "amount": -975.96, "currency": "EUR", "type": "withdrawal"}
    ]

    df = pd.DataFrame(data)

    assert clean_date(df) == 10
    assert clean_date(df) == 5

def test_add():
    assert add(2, 3) == 5

def test_add_2():
    assert add(3, 4) == 7