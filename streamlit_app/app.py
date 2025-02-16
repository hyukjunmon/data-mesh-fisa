import streamlit as st
import requests
import pandas as pd

st.title("📊 데이터 메시 대시보드")

# 데이터 카탈로그 조회
st.header("📖 데이터 카탈로그")
catalog = requests.get("http://catalog_service:7000/api/catalog").json()
for service in catalog["services"]:
    st.subheader(service["name"])
    st.write(service["description"])
    st.json(service["fields"])

# 주문 데이터 조회
st.header("📦 주문 데이터")
orders = requests.get("http://domain_customer:5000/api/orders").json()
st.dataframe(pd.DataFrame(orders))

# 고객 데이터 조회
st.header("👥 고객 데이터")
customers = requests.get("http://domain_order:6000/api/customers").json()
st.dataframe(pd.DataFrame(customers))
