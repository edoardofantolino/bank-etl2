from supabase import create_client, Client
import time
from datetime import datetime, timedelta
import uuid

print("START")

url = "https://yinthengfapdhtvgidoi.supabase.co"
key = "sb_publishable_P4Py0xWkBg2YAU5Wm0fpcw_Nj0--Ju9"

supabase: Client = create_client(url, key)

response = supabase.table("transactions").select("*").execute()

print(response)
print(response.data)
# print(response.error)

new_transaction = {
    "transaction_id": str(uuid.uuid4()),
    "timestamp": datetime.utcnow().isoformat(),
    "account_id": "ACC12345",
    "amount": 150.75,
    "transaction_type": "deposit",
    "is_fraud": False
}

response = supabase.table("transactions").insert(new_transaction).execute()

print(response.data)

print("FINISH")

def load_transactions(transactions):
    response = supabase.table("transactions").insert(transactions).execute()
    print(response.data)
