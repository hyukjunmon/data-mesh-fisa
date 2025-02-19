import streamlit as st
import requests
import pandas as pd
import json

def pretty_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False)

st.title("📊 데이터 메시 대시보드")



departments = ["customer_management", "payment_management"]
st.sidebar.header("📌 검색 가능한 부서 목록")
st.sidebar.write("\n".join(departments))

search_query = st.sidebar.text_input("🔍 검색 (예: payment_management)")
search_button = st.sidebar.button("검색하기")

if search_button:
    if not search_query or "customer_management" in search_query:
        st.header("고객 데이터")
        customers = requests.get("http://customer_management:5000/api/customer").json()
        st.dataframe(pd.DataFrame(customers))
    
    if not search_query or "payment_management" in search_query:
        st.header("결제 데이터")
        payment = requests.get("http://payment_management:6000/api/payment").json()
        st.dataframe(pd.DataFrame(payment))


st.header("📖 데이터 카탈로그")
catalog = requests.get("http://catalog_service:7000/api/catalog").json()
for service in catalog["services"]:
    with st.expander(service["name"]):
        st.write(service["description"])
        st.write("**API URL:**", service["api_url"])
        st.code(pretty_json(service["fields"]), language="json")
