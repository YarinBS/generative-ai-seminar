"""
This module defines the IsAnswerableAgent microagent,
which is responsible for determining if the retrieved data can be used to answer the given question.
"""

from typing import List

from langchain.memory import ConversationBufferMemory

from agent.llm_client import LLMClient
from utils.utils import clean_string

class IsAnswerableAgent:
    """Microagent for determining if the retrieved data can answer the user's question"""

    def __init__(self, llm_client: LLMClient, chat_history: ConversationBufferMemory):
        self.llm_client = llm_client
        self.chat_history = chat_history
        self.system_prompt = """
        You are a verification specialist for Amazon product support.
        Your task is to determine if a user's question can be reliably answered using the provided information.

        Given the available information and the user question, evaluate if the retrieved information contains enough relevant details to provide a helpful, accurate answer.
        Consider:
        1. Does the information directly address the user's question?
        2. Are there specific details about the product features mentioned in the question?
        3. Is the information recent and relevant?
        4. Are there multiple perspectives or experiences shared?

        Respond with only "YES" if the question can be answered, or "NO" if it cannot be answered reliably.
        """

    def check_answerability(self, user_question: str, retrieved_info: List[List[str]]) -> bool:
        """
        Checks if the retrieved information can be used to answer the user question.

        Parameters:
        - user_question: str; The question posed by the user.
        - retrieved_info: List[str]; The context information retrieved for the product.

        Returns:
        - bool; True if the question can be answered, False otherwise.
        """

        if self.chat_history:
            history_string = "; ".join(f"{message.type.upper()}: {message.content}" for message in self.chat_history.chat_memory.messages)
            history_string = f"[{history_string}]."
        else:
            history_string = ""

        complete_human_input = clean_string(f"""
        Based on the following information and the history of the current chat, determine if the user's question can be answered.

        User Question:
        {user_question}

        Retrieved Information:
        {retrieved_info}

        Current chat history:
        {history_string}

        Provide a simple "YES" or "NO" response based on the information's relevance and completeness.
        Do not provide any additional explanations or details other than your "YES" or "NO" answer.
        """)

        if not retrieved_info:  # In the case we got nothing from the vector DB, there's nothing to base our answer on, so we say the answer is not answerable
            return False

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": complete_human_input}
        ]

        response = self.llm_client.generate_response(messages=messages)

        return response.strip().upper() == "YES" or response.strip().upper().startswith("YES")
