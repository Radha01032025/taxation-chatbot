import streamlit as st
import requests

st.title("Taxation Chatbot 💬")
query = st.text_input("Ask me about GST, TDS, or bookkeeping:")

if st.button("Get Answer"):
    url = "http://127.0.0.1:8001/tax_chatbot"  # Removed invalid query string
    response = requests.get(url, params={"query": query})

    if response.status_code == 200:
        result = response.json().get("response", "No response received")
        st.write("### Response:")
        st.write(result)
    else:
        st.error(f"Error fetching response. Status Code: {response.status_code}")