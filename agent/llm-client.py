"""
This module contains the LLMClient class, which is used to interact with the LLM.
"""

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os
import tiktoken
from typing import List, Dict

from utils.token_tracker import log_token_usage

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
            max_tokens=500
        )

        self.embedding_model = AzureOpenAIEmbeddings(
            azure_deployment="team13-embedding",
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=API_KEY,
            openai_api_version=API_VERSION
        )

        self.tokenizer = tiktoken.encoding_for_model("gpt-4o")
    
    def count_tokens(self, text: str) -> int:
        """Counts the number of tokens in the given text using the tokenizer."""
        return len(self.tokenizer.encode(text))
    
    def generate_response(self, messages: List[Dict[str, str]]) -> str:
        """Generates a response from the chat model based on the provided messages."""
        
        langchain_messages = []
        total_input_tokens = 0

        for msg in messages:
            if msg["role"] == "system":
                langchain_messages.append(SystemMessage(content=msg["content"]))
            elif msg["role"] == "human":
                langchain_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_messages.append(AIMessage(content=msg["content"]))
            else:
                langchain_messages.append(HumanMessage(content=msg["content"]))
            
            total_input_tokens += self.count_tokens(msg["content"])
        
        response = self.chat_model.invoke(langchain_messages)
        output_tokens = self.count_tokens(response.content)
        log_token_usage(operation="chat", 
                        input_tokens=total_input_tokens, 
                        output_tokens=output_tokens)
        
        return response.content

    def generate_embeddings(self, texts: List[str]) -> List[float]:
        """Generates embeddings for the given texts."""
        total_input_tokens = sum(self.count_tokens(text) for text in texts)

        if len(texts) == 1:
            embeddings = self.embedding_model.embed_query(texts)
        else:
            embeddings = self.embedding_model.embed_documents(texts)
        
        log_token_usage(operation="embedding", 
                        input_tokens=total_input_tokens)

        return embeddings

client = LLMClient()
