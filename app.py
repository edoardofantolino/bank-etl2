import streamlit as st
# import pandas as pd

# df = pd.read_csv("data/raw/transactions.csv")

st.title("🏦 Banking ETL Dashboard")

st.metric(
    "Numero Transazioni"
    # len(df)
)

st.metric(
    "Volume Totale"
    # f"€ {df['amount'].sum():,.2f}"
)

st.subheader("Transazioni per tipo")
