import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

prompt ="""You are a disease diagnoser. You will be taking symptoms as input and you have to daignose the disease. also provide
also provide small information on the treatment of the disease. here is the symptoms of the disease: 
"""

def generate_gemini(prompt, symptoms):
   model = genai.GenerativeModel("gemini-1.5-flash")
   response = model.generate_content(prompt+symptoms)
   return response.text

st.title("Here is your disease diagnostic")
symptoms=st.text_input("what are your synptoms?")
if symptoms:
    response = generate_gemini(prompt, symptoms)
    st.markdown("Here is the diagnosis")
    st.write(response)