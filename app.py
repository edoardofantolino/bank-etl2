import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

df = pd.read_csv("data/raw/transactions.csv")

st.title("🏦 Banking ETL Dashboard 2")

st.metric("Numero Transazioni", len(df))

st.metric(
    "Volume Totale",
    f"€ {df['amount'].sum():,.2f}"
)

st.metric("Numero Transazioni", df.shape[0])
st.metric("Volume Totale", round(df["amount"].sum(),2))

st.subheader("Transazioni per tipo")

st.bar_chart(
    df.groupby("type")["amount"].sum()
)


daily_volume = (
    df.groupby("date")["amount"]
    .sum()
    .reset_index()
    .sort_values("date")
)

st.subheader("Volume giornaliero")

st.line_chart(
    daily_volume.set_index("date")
)


nulls = df.isna().sum().sum()

duplicates = df.duplicated().sum()

st.subheader("Data Quality")

col1, col2 = st.columns(2)

with col1:
    st.metric("Valori nulli", nulls)

with col2:
    st.metric("Duplicati", duplicates)


df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)

st.line_chart(df)