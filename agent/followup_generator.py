"""
This module defines the FollowUpGenerator class,
which is responsible for generating follow-up questions based on the user's input and the retrieved information.
"""

from typing import List

from llm_client import LLMClient

class FollowUpGenerator:
    """Microagent for generating relevant follow-up questions"""

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.system_prompt = """
        You are a customer experience specialist for Amazon product support.
        Your role is to generate 2-3 relevant follow-up questions that would help users discover more useful information.
        
        Guidelines:
        1. Questions should be related to the user's original question, and to the retrieved information
        2. Focus on practical concerns users might have
        3. Make questions specific and actionable
        4. Avoid generic questions like "Do you have any other questions?"
        5. Questions should help users make informed decisions
        
        Format your response as a simple list of 2-3 questions, one per line, without numbering or bullet points.
        """

    def generate_follow_ups(self, user_input: str, retrieved_info: List[str]) -> str:
        """
        Generates follow-up questions based on the user input and retrieved information.
        """
        
        raise NotImplementedError("Not implemented yet!")