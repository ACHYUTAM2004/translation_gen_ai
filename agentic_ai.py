import streamlit as st
import os
from typing import Dict
import google.generativeai as genai
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

API_KEY = "AIzaSyANWAD8lsGZeRHFuJ9V_MnH2DCHzFZmtEg"
genai.configure(api_key=API_KEY)

def translate_text(ip_text,tgt_lang):
    print(f"Tool translate_text called to translate sentence to {tgt_lang}")
    model='gemini-1.5-flash-latest'
    prompt=f"Translate the following text to {tgt_lang}, donot provide any comments or explanation. Text is {ip_text}"
    response=model.generate_content(prompt)
    if response.candidates:
        translated_text=response.candidates[0].content.parts[0].text.strip()
        return ("Translated text: ",translated_text)
    else:
        return ("Error! translation failed")
    
translation_agent=LlmAgent(
    model='gemini-1.5-flash-latest',
    name="translation_agent",
    description="An agent that translates text by using translate_text tool",
    instruction="""
    You are a helpful translation assistant. Your job is to understand the user's
    request and use the 'translate_text' tool to perform the translation.
    Once the tool returns the translated text, output it directly to the user
    as your final answer.
    """,
    tools=[translate_text]
)   

runner=Runner(
    agent=translation_agent,
    app_name="translation_app",
    session_service=InMemorySessionService()
)

def run_translation(query):
    print(f"user query: {query}")
    user_input=Content(role="user",parts=[Part(text=query)])
    events=runner.run(
        user_id="test_user",
        session_id="test_session",
        new_message=user_input
    )
    final_response="No response from agent"
    for event in events:
        if event.is_final_response():
            final_response=event.content.parts[0].text
            break
    return final_response
# ... (your existing translate_text, LlmAgent, Runner setup code) ...

st.title("AI-Powered Translation Assistant")

user_query = st.text_input("Enter your translation request (e.g., 'Translate 'Hello' to French.'):")

if st.button("Translate"):
    if user_query:
        with st.spinner("Translating..."):
            run_translation(user_query) # This will print to console, you'd modify run_translation to return the string
            # For Streamlit, you'd likely modify run_translation to return the final_response string
            # and then st.write(final_response) here
    else:
        st.warning("Please enter some text to translate.")

# In the Streamlit button block:
if st.button("Translate"):
    if user_query:
        with st.spinner("Translating..."):
            translated_text = run_translation(user_query)
            st.success("Translated Text:")
            st.write(translated_text)
    else:
        st.warning("Please enter some text to translate.")