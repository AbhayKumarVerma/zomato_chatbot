# interface/app.py

import streamlit as st
import importlib.util
import sys
import os

left, center, right = st.columns([1, 6, 1])
# Place the title only in the center column
center.title("Zomato Chatbot")
# 1. Specify the full path to chatbot.py
CHATBOT_PATH = r"C:\Users\abhay verma\OneDrive\Desktop\zomato_new\zomato_gen_ai\chatbot\chatbot.py"

# 2. Dynamically load the module from that path
spec = importlib.util.spec_from_file_location("chatbot_module", CHATBOT_PATH)  # load spec from file :contentReference[oaicite:0]{index=0}
chatbot_module = importlib.util.module_from_spec(spec)                           # create a new module object :contentReference[oaicite:1]{index=1}
spec.loader.exec_module(chatbot_module)                                           # execute the module in its namespace :contentReference[oaicite:2]{index=2}

# 3. Grab the get_response function
get_response = chatbot_module.get_response

# Streamlit UI
user_query = st.text_input("")
if st.button("Get Response"):
    if user_query:
        response = get_response(user_query)
        st.write("**Response:**", response)
    else:
        st.write("⚠️ Please enter a question.")
