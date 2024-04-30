import os
import streamlit as st
from st_pages import Page, show_pages, hide_pages
from llm_utils.login import AzureKeyHandler, OpenaiKeyHandler

st.set_page_config(
    page_title="IRB Assistant",
    page_icon="🤖",
)
# Initalize state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


def log_in():
    api_key = st.session_state["api_key"]
    os.environ["OPENAI_API_KEY"] = api_key

    import IRB_Assistant_config.config as irb_assistant_config


    if api_key_type == "Azure":
        key_handler = AzureKeyHandler(irb_assistant_config.azure_chat_config, 
                                        irb_assistant_config.azure_pubmed_chat_config) 
        
        initialized = key_handler.initialize_api_key(api_key, irb_assistant_config.AZURE_END_POINT)

    elif api_key_type == "OpenAI":
        key_handler = OpenaiKeyHandler(irb_assistant_config.openai_chat_config, 
                                        irb_assistant_config.openai_pubmed_chat_config)
        initialized = key_handler.initialize_api_key(api_key, irb_assistant_config.OPENAI_END_POINT)

    else:
        st.error("Select the API key type.")


    # print(initialized)
    if initialized:
        st.session_state.logged_in = True 
        st.session_state.chat_config = key_handler.get_chat_function()
        st.session_state.pubmed_chat_config = key_handler.get_pubmed_chat_function()

if not st.session_state["logged_in"]:
    st.title("Bring your own key")
        
    api_key_type = st.selectbox('Select the type of your API key', ('OpenAI', 'Azure'))
    api_key = st.text_input("Enter your API key", key = "api_key", type="password", on_change=log_in)

else: 
    st.title("Home")
    st.write("Welcome!")
    st.markdown("Navigate using the sidebar")
    show_pages(
    [
        Page("streamlit/1_irb_assistant_app.py", "IRB Assistant ⚖️"),
        Page("streamlit/2_simplify_text_app.py", "Simplify Text 🔠"),

    ]
)


