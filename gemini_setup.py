import google.generativeai as genai

try:
    # Replace with your actual API key
    genai.configure(api_key="AIzaSyBxjk6iFYUHg4SC_Wfr_R8RaYEv72n9shg")
    print("✅ Gemini API is set up successfully!")
except Exception as e:
    print("❌ Error:", e)

