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
    st.write("다음은 예시입니다.")
    st.write(service["api_url"])
    st.json(service["fields"])

# 고객 데이터 조회
st.header("고객 데이터")
customers = requests.get("http://customer_management:5000/api/customer").json()
st.dataframe(pd.DataFrame(customers))

# 결제 데이터 조회
st.header("결제 데이터")
payment = requests.get("http://payment_management:6000/api/payment").json()
st.dataframe(pd.DataFrame(payment))
