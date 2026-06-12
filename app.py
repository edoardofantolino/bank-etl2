import streamlit as st
# import pandas as pd

# df = pd.read_csv("data/raw/transactions.csv")

st.title("🏦 Banking ETL Dashboard")

st.metric("Numero Transazioni")

static_value = 5
st.metric(
    "Volume Totale"
    f"€ {static_value}"
)

st.subheader("Transazioni per tipo")
