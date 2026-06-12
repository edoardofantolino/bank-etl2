import streamlit as st
# import pandas as pd

# df = pd.read_csv("data/raw/transactions.csv")

st.title("🏦 Banking ETL Dashboard 2")

st.metric("Numero Transazioni", 5)

static_value = 5
st.metric(
    "Volume Totale"
    f"€ {static_value}", static_value
)

st.subheader("Transazioni per tipo")
