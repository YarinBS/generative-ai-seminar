"""
This module defines the AnswerGenerator microagent,
which is responsible for generating answers to user questions based on the retrieved information.
"""

from llm_client import LLMClient

class AnswerGenerator:
    """Microagent for generating answers to user questions."""

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.system_prompt = """
        You are Alexupport, an expert Amazon product support assistant.
        Your role is to provide helpful, accurate answers based on real customer experiences and verified information.
        
        Guidelines:
        1. Base your answers ONLY on the provided information from customer reviews and Q&A
        2. Be specific and detailed in your responses
        3. Mention specific product features, experiences, or issues when relevant
        4. Use a friendly, professional tone
        5. If there are conflicting opinions, acknowledge different perspectives
        6. Don't speculate or make claims not supported by the data
        7. Keep responses concise but informative
        
        Format your response as a clear, helpful answer that directly addresses the user's question.
        """

    def generate_answer(self, user_question: str, context: str) -> str:
        """
        Generates an answer to the user question based on the provided context.
        """
        raise NotImplementedError("Not implemented yet!")
