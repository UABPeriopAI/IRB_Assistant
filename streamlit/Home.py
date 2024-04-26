import streamlit as st
from st_pages import Page, show_pages, hide_pages
import os
import requests
import IRB_Assistant_config.config as irb_assistant_config
from IRB_Assistant.login import log_in

st.set_page_config(
    page_title="IRB Assistant",
    page_icon="🤖",
)
# Initalize state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Initalize state
if "api_key" not in st.session_state:
    st.session_state["api_key"] = None

if not st.session_state["logged_in"]:
    # hide_pages(["IRB Assistant", "Literature Assistant", "Simplify Text"])
    st.title("Bring your own key")
        
    api_key_type = st.selectbox('Select the type of your API key', ('OpenAI', 'Azure'))
    api_key = st.text_input("Enter your API key", type="password", on_change=log_in(api_key_type))

else: 
    st.title("Home")
    st.write("Welcome!")
    st.markdown("Navigate using the sidebar")
    show_pages(
    [
        Page("streamlit/1_irb_assistant_app.py", "IRB Assistant ⚖️"),
        Page("streamlit/3_simplify_text_app.py", "Simplify Text 🔠"),

    ]
)


