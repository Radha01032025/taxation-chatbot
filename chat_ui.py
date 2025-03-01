import streamlit as st
import google.generativeai as genai
import os

# ✅ Load API Key securely from environment variables
API_KEY = os.getenv("AIzaSyDbCzV8brNCoEJy0tC-7z9P39MAldU0J78")
genai.configure(api_key=API_KEY)

# ============================
# ✅ AI Integration with Gemini
# ============================
def chat_with_gemini(prompt):
    """Send a user query to the Google Gemini API and get a response."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# ============================
# ✅ Streamlit Web Interface
# ============================
st.title("💬 AI-Powered Taxation Chatbot")
st.write("Ask me about **GST, TDS, Income Tax, Due Dates, or Tax Filing!**")

# ✅ Display Profile Photo in Sidebar
st.sidebar.image("images/profile.jpg", caption="Amit Bhadra Srivastava", use_container_width=True)

# User Input
query = st.text_input("Enter your query:")

if st.button("Get Answer"):
    if query.strip():
        response = chat_with_gemini(query)
        st.write("### Response:")
        st.write(response)
    else:
        st.warning("Please enter a valid question.")

# ✅ About Section
st.sidebar.subheader("ℹ️ About this Chatbot")
st.sidebar.write("👨‍⚖️Created By :**Amit Bhadra Srivastava**")
st.sidebar.write("**Purpose:** To answer Taxation & Accounting related queries - for an interactive UI.")
st.sidebar.write("📌Firm Name: **Bhadra & Company**")
st.sidebar.write("⚖️ **Services:** Legal & Taxation")
st.sidebar.write("📍**Location:** Gurugram & Kanpur")
st.sidebar.markdown("---")  # Adds a separator