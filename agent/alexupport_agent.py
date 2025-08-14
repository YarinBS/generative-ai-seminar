"""
Main Alexupport agent
This module contains the main agent which orchestrates the other microagents
"""

from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage

from agent.answer_generator import AnswerGenerator
from agent.followup_generator import FollowUpGenerator
from agent.input_refiner import InputRefiner
from agent.is_answerable_agent import IsAnswerableAgent
from agent.is_relevant_agent import IsRelevantAgent
from agent.llm_client import LLMClient

LLM_CLIENT = LLMClient()

class AlexupportAgent:
    """Main Alexupport agent"""

    def __init__(self):

        self.introduction = """
        Hi! I am Alexupport 🤖, your Amazon AI assistant. I am here to answer your questions regarding different Amazon products.
        Start by choosing a product, and then ask me anything about it!
        """

        self.chat_start = "Let's have a chat about {product_title}.\nAsk me anything!"

        self.memory = ConversationBufferMemory()

        # Initializing all microagents
        self.input_refiner = InputRefiner(llm_client=LLM_CLIENT)
        self.is_answerable_agent = IsAnswerableAgent(llm_client=LLM_CLIENT)
        self.answer_generator = AnswerGenerator(llm_client=LLM_CLIENT, chat_history=self.memory)
        self.followup_generator = FollowUpGenerator(llm_client=LLM_CLIENT)
        self.is_relevant_generator = IsRelevantAgent(llm_client=LLM_CLIENT)

    def get_agent_introduction(self) -> str:
        """Displays the agent introduction and instructions to the user upon activation"""
        return self.introduction

    def get_agent_chat_start(self, product_title: str) -> str:
        """Displays the initial chat prompt to the user"""
        if product_title != "No title found":
            return self.chat_start.format(product_title=product_title)
        return "Let's have a chat about your product.\nAsk me anything!"

    def answer_user_query(self, user_query: str) -> str:
        """Main Alexupport pipeline"""
        # Step 0 - Clear previous chat history, if exists
        self.memory.clear()

        #TODO: Implement the complete pipeline

        raise NotImplementedError()
