import streamlit as st
import os
import requests
import IRB_Assistant_config.config as irb_assistant_config

# TODO: move everything to llm_utils
def log_in(api_key_type):
    api_key = st.session_state["api_key"]
    # print("api_key", api_key)

    if api_key is not None:
        if api_key_type == "Azure":
            key_handler = AzureKeyHandler() 
            
        elif api_key_type == "OpenAI":
            key_handler = OpenaiKeyHandler()

        else:
            st.error("Select the API key type.")


        initialized = key_handler.initialize_api_key(api_key)

        print(initialized)
        if initialized:
            st.session_state.logged_in = True 
            st.session_state.chat_config = key_handler.get_chat_function()
            st.session_state.pubmed_chat_config = key_handler.get_pubmed_chat_function()
            

class BYOK_Handler():
    def __init__(self):
        self.api_key_type = None
        self.api_key = None
        self.CHAT = None
        self.PUBMED_CHAT = None


    def _api_key_validation(self, api_key):
        pass

    def initialize_api_key(self, api_key):
        pass

    def get_chat_function(self):
        # print('parent - ', self.CHAT)
        return self.CHAT
    
    def get_pubmed_chat_function(self):
        return self.PUBMED_CHAT


class AzureKeyHandler(BYOK_Handler):

    def _api_key_validation(self, api_key):
        # TODO: timeout
        response = requests.get('https://nlp-ai-svc.openai.azure.com/openai/models?api-version=2024-02-01', headers={ 'api-key': api_key})

        if response.status_code == 200:
            return True
        else:
            return False

    def initialize_api_key(self, api_key):
        if self._api_key_validation(api_key):
            # TODO: generalize this - next 2 lines
            st.success('API key is valid.')
            os.environ["OPENAI_API_KEY"] = api_key
            self.CHAT = irb_assistant_config.azure_chat_config
            self.PUBMED_CHAT = irb_assistant_config.azure_pubmed_chat_config
            return True

        else:
            st.error('API key is invalid.')
            return False


class OpenaiKeyHandler(BYOK_Handler):


    def _api_key_validation(self, api_key):
                # TODO: timeout

        response = requests.get('https://api.openai.com/v1/engines', headers={ 'Authorization': 'Bearer ' + api_key})

        if response.status_code == 200:
            return True
        else:
            return False
        
    def initialize_api_key(self, api_key):
        if self._api_key_validation(api_key):
            st.success('API key is valid.')
            os.environ["OPENAI_API_KEY"] = api_key
            self.CHAT = irb_assistant_config.openai_chat_config
            self.PUBMED_CHAT = irb_assistant_config.openai_pubmed_chat_config
            return True
        else:
            st.error('API key is invalid.')
            return False



