from loguru import logger
from agents.agent import Agent


class GreetingAgent(Agent):
    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["user_input"],
                    "template": """
                    The user said: {user_input}
                    
                    At the end of the loop, you output an Answer.
                    check if the input is related to any region in the province of Quebec.
                    If it is not related to Quebec, return "not related".
                    If it is realated to Quebec, then classify it as "immigration", "education", or "other".
                    
                    Your available actions are:

                    check_quebec_relevance:
                    e.g. check_quebec_relevance: "What are the requirements for Montreal immigration?"
                    if the input is not related to Quebec return "not related", otherwise classify_quebec_input action.

                    classify_quebec_input:
                    e.g. classify_quebec_input: "What are the requirements for Montreal immigration?"
                    Returns one of the following categories: "immigration", "education", or "other".
                    
                    output: "immigration", "education", "other" or "not related"
                    do not return natural language text here, just the category.
                    """,
                }
            )

        except Exception as e:
            logger.error(f"Error initializing GreetingAgent: {e}")
            raise

    def greet(self, user_input: str):
        try:
            return self.run(self.chain, user_input=user_input)
        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise
