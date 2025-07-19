"""
This module defines the IsRelevantAgent microagent,
which is responsible for determining the relevance of the generated response
to the user's question.
"""

from llm_client import LLMClient

class IsRelevantAgent:
    """Microagent for determining the relevance of the generated response."""

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.system_prompt = """
        You are a quality assurance specialist for Amazon product support.
        Your task is to verify if a generated answer is relevant, accurate, and helpful.
        
        Original question: {question}
        
        Retrieved information:
        {retrieved_info}
        
        Generated answer: {generated_answer}
        
        Evaluate the answer based on:
        1. Does it directly address the user's question?
        2. Is it based on the provided information?
        3. Is it helpful and informative?
        4. Does it avoid speculation or generic responses?
        5. Is it written in a clear, professional tone?
        
        Respond with only "YES" if the answer is good, or "NO" if it needs improvement.
        """

    def assess_relevance(self, user_question: str, generated_response: str) -> str:
        """
        Assesses the relevance of the generated response to the user question.
        """
        
        raise NotImplementedError("Not implemented yet!")