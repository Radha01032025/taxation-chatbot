import google.generativeai as genai
import requests
import os

# ✅ Load API Key securely from environment variables
API_KEY = os.getenv("AIzaSyDbCzV8brNCoEJy0tC-7z9P39MAldU0J78")

# ✅ Configure Gemini API
genai.configure(api_key=API_KEY)

# ✅ Set API URL for Gemini (alternative way using requests)
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={API_KEY}"

# ============================
# ✅ Tax Calculation Functions
# ============================
def calculate_gst(amount, gst_rate):
    gst_amount = (amount * gst_rate) / 100
    total_amount = amount + gst_amount
    return {"GST Amount": gst_amount, "Total Amount": total_amount}

def calculate_tds(amount, tds_rate):
    tds_amount = (amount * tds_rate) / 100
    net_payment = amount - tds_amount
    return {"TDS Amount": tds_amount, "Net Payment": net_payment}

def calculate_income_tax(income):
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.2
    else:
        tax = 112500 + (income - 1000000) * 0.3
    return {"Income Tax": tax}

def get_due_dates():
    return {
        "GST Returns": {"GSTR-1": "11th of Next Month", "GSTR-3B": "20th of Next Month"},
        "TDS Returns": {"TDS Payment": "7th of Every Month", "TDS Filing": "31st of Next Quarter"},
        "Income Tax Filing": {"Individuals": "31st July", "Companies": "30th September"}
    }

# ==============================
# ✅ AI Integration with Gemini
# ==============================
def chat_with_gemini(prompt):
    """Sends query to Google Gemini API and returns AI-generated response."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in AI response: {str(e)}"

# ============================
# ✅ Chatbot Logic
# ============================
def taxation_chatbot(user_input):
    try:
        # Tax Calculations
        if "gst" in user_input.lower():
            parts = user_input.split()
            if len(parts) >= 3:
                amount = float(parts[1])
                gst_rate = float(parts[2])
                return calculate_gst(amount, gst_rate)
            return "Invalid format. Use: 'gst <amount> <rate>'"

        elif "tds" in user_input.lower():
            parts = user_input.split()
            if len(parts) >= 3:
                amount = float(parts[1])
                tds_rate = float(parts[2])
                return calculate_tds(amount, tds_rate)
            return "Invalid format. Use: 'tds <amount> <rate>'"

        elif "income tax" in user_input.lower():
            parts = user_input.split()
            if len(parts) >= 2:
                income = float(parts[1])
                return calculate_income_tax(income)
            return "Invalid format. Use: 'income tax <income>'"

        elif "due date" in user_input.lower():
            return get_due_dates()

        # AI-Powered Gemini Chat
        else:
            return chat_with_gemini(user_input)

    except Exception as e:
        return {"error": str(e)}

# ============================
# ✅ Run the Chatbot
# ============================
if __name__ == "__main__":
    print("\n💬 Gemini AI Taxation Chatbot | Type 'exit' to quit\n")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Goodbye! 👋")
            break
        response = taxation_chatbot(user_query)
        print(f"Bot: {response}\n")