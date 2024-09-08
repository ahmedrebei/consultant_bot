from loguru import logger
from agents.agent import Agent


class GreetingAgent(Agent):
    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["query"],
                    "template": """
                    You are a classifier that only responds with one of the following categories: "not related", "other", "immigration", or "education". Follow these rules:

                    If the query mentions topics, locations or institutions outside of Quebec, respond with "not related".
                    If the query is related to immigration in Quebec, respond with "immigration".
                    If the query is related to education in Quebec, respond with "education".
                    If the query is related to Quebec but does not involve immigration or education, respond with "other".
                    If none of the conditions apply, respond with "not related".
                    Example queries:

                    "How do I apply for a visa to Quebec?": immigration
                    "What are the universities in Montreal?": education
                    "How is the weather in Quebec?": other
                    "Tell me about universities in Toronto.": not related
                    
                    Here is the user's input: {query}

                    Classify the input according to the rules above.
                    do not return natural language text here, just the category.
                    
                    your classification:
                    """
                }
            )

        except Exception as e:
            logger.error(f"Error initializing GreetingAgent: {e}")
            raise

    def greet(self, query: str) -> str:
        try:
            return self.run(self.chain, query=query)
        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise
