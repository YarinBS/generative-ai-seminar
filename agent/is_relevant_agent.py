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
        Given a question, and an answer your task is to verify if a generated answer is relevant, accurate, and helpful.

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

        complete_human_input = f"""
        Based on the following information, determine if the generated answer is relevant and helpful.
        
        Original question: {user_question}
        
        Generated answer: {generated_response}

        Provide a simple "YES" or "NO" response based on the answer's relevance and helpfulness.
        Do not provide any additional explanations or details other than your "YES" or "NO" answer.
        """

        response = self.llm_client.generate_response(messages=[
            {"role": "user", "content": complete_human_input}
        ])

        return response.strip().upper() == "YES"
