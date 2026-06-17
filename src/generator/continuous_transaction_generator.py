import time
from transaction_generator import *
from datetime import timedelta
from supabase import create_client, Client
import uuid

url = "https://yinthengfapdhtvgidoi.supabase.co"
key = "sb_publishable_P4Py0xWkBg2YAU5Wm0fpcw_Nj0--Ju9"
supabase: Client = create_client(url, key)


OUTPUT_FILE = "../../data/raw/continuous_transactions.csv"
current_timestamp = datetime.now() - timedelta(days=30)

for i in range(2000):        

    print("transaction ", i)

    with open(OUTPUT_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if current_timestamp.weekday() >= 5:  # Sabato o Domenica
            delta_seconds = random.randint(60, 1800)      # 1-30 minuti
        else:
            delta_seconds = random.randint(60, 3600)     # 1-60 minuti

        current_timestamp += timedelta(seconds=delta_seconds)

        timestamp = current_timestamp.strftime(
            "%Y/%m/%d %H:%M:%S"
        )

        tx_type = random.choice(types)

        i_date = timestamp
        i_account = random.choice(accounts)
        i_amount = random_amount(tx_type)
        i_currency = random.choice(currencies)


        is_duplicate = random.randint(1, 100)

        is_duplicate = 2 if is_duplicate == 1 else 1

        for _ in range(is_duplicate):
            writer.writerow([
                i,
                i_date,
                i_account,
                i_amount,
                i_currency,
                tx_type
            ])


            new_transaction = {
                "transaction_id": str(uuid.uuid4()),
                "timestamp": i_date,
                "account_id": i_account,
                "amount": i_amount,
                "transaction_type": tx_type,
                "is_fraud": False
            }

            response = supabase.table("transactions").insert(new_transaction).execute()


        


    
    # save_to_sqlite()

    # fraud_detection()

    time.sleep(0.2)