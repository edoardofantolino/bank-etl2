import pandas as pd

print("We can do lots of stuff with pandas")
df = pd.read_csv("../data/raw/transactions.csv")

print(df.head())