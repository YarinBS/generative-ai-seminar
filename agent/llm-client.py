"""
This module contains the LLMClient class, which is used to interact with the LLM.
"""

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
import os

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY is not set, add it to the .env file")

CHAT_DEPLOYMENT_NAME = "team13-gpt4o"
EMBEDDING_DEPLOYMENT_NAME = "team13-embedding"

class LLMClient:
    """
    General LLM client class to be used across all microagents in the project
    """

    def __init__(self):
        
        
        self.chat_model = AzureChatOpenAI(
            azure_deployment=CHAT_DEPLOYMENT_NAME,
            api_key=api_key,
            openai_api_type="azure"
        )

        self.embedding_model = AzureOpenAIEmbeddings(

        )
