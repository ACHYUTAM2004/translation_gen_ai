import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("🌍 Language Translator (Gemini)")

text = st.text_input("Enter text to translate:")
target_lang = st.text_input("Translate to (e.g., Hindi, Spanish, French):")

if st.button("Translate"):
    if text and target_lang:
        with st.spinner("Translating..."):
            prompt = f"Translate the following text to {target_lang}, do not provide any comments or explanation. Text is: {text}"
            try:
                response = model.generate_content(prompt)
                output = response.text.strip()
                st.success(output)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter both text and target language.")
