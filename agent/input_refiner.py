"""
This module defines the InputRefiner microagent,
which is responsible for refining and enriching user questions
"""

from langchain.memory import ConversationBufferMemory

from agent.llm_client import LLMClient

class InputRefiner:
    """Microagent for refining and enriching user questions."""

    def __init__(self, llm_client: LLMClient, chat_history: ConversationBufferMemory):
        self.llm_client = llm_client
        self.chat_history = chat_history
        self.system_prompt =  """
        You are a question refinement specialist for Amazon product support.

        Given a question from the user, your task is to:
        1. Fix typos and grammatical errors in the user question
        2. Expand abbreviations and clarify ambiguous terms
        3. Maintain the original intent while making the question more specific

        Return only the refined question without any explanations or additional text.
        """

    def refine_input(self, user_input: str) -> str:
        """
        Refines the user input by adding context or modifying it to improve LLM responses.
        """

        complete_human_input = f"""
        Refine the following user question to improve clarity and specificity.
        User Question: {user_input}
        """

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": complete_human_input}
        ]

        response = self.llm_client.generate_response(messages=messages)

        if self.chat_history:
            # If we have chat history, we can add it to the context
            response = None  #TODO: Implement chat history context handling
        
        return response.strip()
