import csv
import random
from datetime import datetime, timedelta

# Set number of transactions
N = 10000

OUTPUT_FILE = "transactions.csv"

# =========================
# FIXED PARAMETERS
# =========================
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 5, 31)

## Next step would be to improve the generations of the IBAN codes
accounts = [
    "IT1234", "IT2345", "IT3456", "IT4567",
    "IT5678", "IT6789", "IT7890", "IT8901"
]

# currencies = ["EUR", "USD"]
currencies = ["EUR"]
types = ["withdrawal", "deposit", "transfer"]

# =========================
# DATE GENERATOR
# =========================
def random_date():
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# =========================
# AMOUNT GENERATOR
# =========================
def random_amount(tx_type):
    if tx_type == "deposit":
        return round(random.uniform(50, 5000), 2)
    elif tx_type == "withdrawal":
        return round(-random.uniform(20, 2000), 2)
    else:  # transfer
        return round(random.uniform(-1500, 1500), 2)

# =========================
# GENERATION
# =========================
with open(OUTPUT_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)

    # header
    writer.writerow(["transaction_id", "date", "account", "amount", "currency", "type"])

    for i in range(1, N + 1):
        tx_type = random.choice(types)

        writer.writerow([
            i,
            random_date().strftime("%d/%m/%Y"),
            random.choice(accounts),
            random_amount(tx_type),
            random.choice(currencies),
            tx_type
        ])

print(f"Generated {N} transactions in {OUTPUT_FILE}")