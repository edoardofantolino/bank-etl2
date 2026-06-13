import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
from streamlit_autorefresh import st_autorefresh
from supabase import create_client

url = "https://yinthengfapdhtvgidoi.supabase.co"
key = "sb_publishable_P4Py0xWkBg2YAU5Wm0fpcw_Nj0--Ju9"

supabase = create_client(url, key)

response = supabase.table("transactions").select("*").execute()
data = response.data
df = pd.DataFrame(data)

st_autorefresh(
    interval=5000,
    key="refresh"
)

# df = pd.read_csv("data/raw/continuous_transactions.csv")

st.title("🏦 Banking ETL Dashboard 2")

st.metric("Numero Transazioni", len(df))

st.metric(
    "Volume Totale",
    f"€ {df['amount'].sum():,.2f}"
)

single_volume = (
    df.groupby("timestamp")["amount"]
    .sum()
    .reset_index()
)

"""
st.subheader("Singola transazione")

st.line_chart(
    single_volume.set_index("timestamp")
)


df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    format="mixed"
)

daily_volume = (
    df.groupby(df["timestamp"].dt.date)["amount"]
    .sum()
    .reset_index()
)

st.subheader("Volume giornaliero")

st.line_chart(
    daily_volume.set_index("timestamp")
)

daily_volume = (
    df.groupby(df["timestamp"].dt.date)["amount"]
    .sum()
    .reset_index()
)



st.subheader("Numero transazioni giornaliere")

daily_volume = (
    df.groupby(df["timestamp"].dt.date)["amount"]
    .count()
    .reset_index()
)

st.line_chart(
    daily_volume.set_index("timestamp")
)


nulls = df.isna().sum().sum()

duplicates = df.duplicated().sum()

st.subheader("Data Quality")

col1, col2 = st.columns(2)

with col1:
    st.metric("Valori nulli", nulls)

with col2:
    st.metric("Duplicati", duplicates)


st.subheader("Transazioni per tipo")

st.bar_chart(
    df.groupby("transaction_type")["amount"].sum()
)

# df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

# st.area_chart(df)

# st.line_chart(df)
"""