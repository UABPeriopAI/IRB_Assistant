# config.py
# import logging
from pathlib import Path

from langchain.chat_models import ChatOpenAI
from langchain.chat_models import AzureChatOpenAI


# Development Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
LOGS_DIR = Path(BASE_DIR, "logs")

# Data Directories
DATA_DIR = Path("/data/DATASCI")
RAW_DATA = Path(DATA_DIR, "raw")
INTERMEDIATE_DIR = Path(DATA_DIR, "intermediate")
RESULTS_DIR = Path(DATA_DIR, "results")

# DATA Files

# Assets
ASSETS_DIR = Path(BASE_DIR, "assets")
TEMPLATE = Path(ASSETS_DIR, "numbered_template.docx")

chat_configs = {}

# END points
AZURE_END_POINT = 'https://nlp-ai-svc.openai.azure.com'
OPENAI_END_POINT = 'https://api.openai.com/v1/engines'

azure_chat_config =  AzureChatOpenAI(
    openai_api_base=AZURE_END_POINT,
    openai_api_version="2023-06-01-preview",
    deployment_name="ChatGPT4",
    openai_api_type="azure",
    temperature=0,
    model_name="gpt-4"
)


azure_pubmed_chat_config = AzureChatOpenAI(
    openai_api_base=AZURE_END_POINT,
    openai_api_version="2023-06-01-preview",
    deployment_name="ChatGPT4",
    openai_api_type="azure",
    temperature=0.9,
    model_name="gpt-4")



openai_chat_config = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", request_timeout=300)

openai_pubmed_chat_config = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", request_timeout=300)




# lit search
MAX_PUBMED_RESULTS = 50
MIN_ARTICLES = 10

