from loguru import logger
from agents.agent import Agent


class SummarizationAgent(Agent):
    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["query", "conversation_history"],
                    "template": """
                    You are an AI assistant. Here is the conversation so far. 
                    Your task is to summarize the key points from the conversation, focusing on the most important details that are relevant to answering the user's current query. 
                    If the conversation switches topics, keep only the most recent relevant information.
                    Make the summary concise and focused on the user’s intent.

                    Conversation history:
                    {conversation_history}

                    Current user query:
                    {query}

                    Summary of conversation history:
                    """,
                }
            )
        except Exception as e:
            logger.error(f"Error initializing SummarizationAgent: {e}")
            raise

    def summarize(self, query: str, conversation_history: str) -> str:
        try:
            return self.run(
                self.chain, query=query, conversation_history=conversation_history
            )
        except Exception as e:
            logger.error(f"Error in SummarizationAgent greet: {e}")
            raise
