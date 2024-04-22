import streamlit as st
from st_pages import Page, show_pages, hide_pages
import os
import requests
import IRB_Assistant_config.config as irb_assistant_config
from login_handler import AzureKeyHandler, OpenaiKeyHandler

st.set_page_config(
    page_title="IRB Assistant",
    page_icon="🤖",
)
# Initalize state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


def log_in():
    api_key = st.session_state["api_key"]
    # print("api_key", api_key)

    if api_key_type == "Azure":
        key_handler = AzureKeyHandler() 
        
    elif api_key_type == "OpenAI":
        key_handler = OpenaiKeyHandler()

    else:
        st.error("Select the API key type.")

    initialized = key_handler.initialize_api_key(api_key)
    if initialized:
        st.session_state.logged_in = True 
        st.session_state.chat_config = key_handler.get_chat_function()
        st.session_state.pubmed_chat_config = key_handler.get_pubmed_chat_function()


if not st.session_state["logged_in"]:
    # hide_pages(["IRB Assistant", "Literature Assistant", "Simplify Text"])
    st.title("Bring your own key")
        
    api_key_type = st.selectbox('Select the type of your API key', ('OpenAI', 'Azure'))
    api_key = st.text_input("Enter your API key", key="api_key", type="password", on_change=log_in)

else: 
    st.title("Home")
    st.write("Welcome!")
    st.markdown("Navigate using the sidebar")
    show_pages(
    [
        Page("streamlit/1_irb_assistant_app.py", "IRB Assistant ⚖️"),
        Page("streamlit/2_literature_assistant_app.py", "Literature Assistant 📚"),
        Page("streamlit/3_simplify_text_app.py", "Simplify Text 🔠"),

    ]
)


