"""
This module contains the LLMClient class, which is used to interact with the LLM.
"""

from dotenv import load_dotenv
import tiktoken
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
import os

tiktoken.encoding_for_model("gpt-4o")

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is not set, add it to the .env file")

AZURE_OPENAI_ENDPOINT = "https://096290-oai.openai.azure.com"
API_VERSION = "2023-05-15"


class LLMClient:
    """
    This is a general LLM client class to be used across all microagents in the project.
    It initializes the chat model and embedding model using Azure OpenAI and provides methods for chat/embedding generation, 
    as well as tokens count.
    """

    def __init__(self):
        """Initializes the LLMClient with Azure OpenAI models"""
        self.chat_model = AzureChatOpenAI(
            azure_deployment="team13-gpt4o",
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=API_KEY,
            openai_api_version=API_VERSION,
            openai_api_type="azure"
        )

        self.embedding_model = AzureOpenAIEmbeddings(
            azure_deployment="team13-embedding",
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=API_KEY,
            openai_api_version=API_VERSION,
            openai_api_type="azure"
        )

        self.tokenizer = tiktoken.encoding_for_model("gpt-4o")
    
    def count_tokens(self, text: str) -> int:
        """Counts the number of tokens in the given text using the tokenizer."""
        return len(self.tokenizer.encode(text))
    
    def generate_response(self, messages):
        """Generates a response from the chat model based on the provided messages."""
        pass

    def generate_embedding(self, text: str):
        """Generates an embedding for the given text."""
        pass

client = LLMClient()
