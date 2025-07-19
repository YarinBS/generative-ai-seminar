"""
This module defines the IsAnswerableAgent microagent,
which is responsible for determining if the retrieved data can be used to answer the user's question.
"""

from typing import List

from llm_client import LLMClient

class IsAnswerableAgent:
    """Microagent for determining if the retrieved data can answer the user's question."""

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.system_prompt = """
        You are a verification specialist for Amazon product support.
        Your task is to determine if a user's question can be reliably answered using the provided information.
        
        Available information:
        {retrieved_info}
        
        User question:
        {question}
        
        Evaluate if the retrieved information contains enough relevant details to provide a helpful, accurate answer.
        Consider:
        1. Does the information directly address the user's question?
        2. Are there specific details about the product features mentioned in the question?
        3. Is the information recent and relevant?
        4. Are there multiple perspectives or experiences shared?
        
        Respond with only "YES" if the question can be answered, or "NO" if it cannot be answered reliably.
        """

    def check_answerability(self, user_question: str, retrieved_info: List[str]) -> str:
        """
        Checks if the retrieved information can be used to answer the user question.
        """
        
        raise NotImplementedError("Not implemented yet!")