"""
This module defines the InputRefiner microagent,
which is responsible for refining and enriching user questions
"""


from llm_client import LLMClient

class InputRefiner:
    """Microagent for refining and enriching user questions."""

    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.system_prompt =  """
        You are a question refinement specialist for Amazon product support.

        Given a question from the user, your task is to:
        1. Fix typos and grammatical errors in the user question
        2. Expand abbreviations and clarify ambiguous terms
        3. Maintain the original intent while making the question more specific
        4. If chat history is provided, incorporate relevant context

        Return only the refined question without any explanations or additional text.
        """

    def refine_input(self, user_input: str) -> str:
        """
        Refines the user input by adding context or modifying it to improve LLM responses.
        """

        raise NotImplementedError("Not implemented yet!")
