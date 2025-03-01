import requests

query = "calculate GST"
response = requests.get(f"http://127.0.0.1:8000/tax_chatbot?query={query}")

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)