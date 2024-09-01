from loguru import logger
from agents.agent import Agent


class GradingAgent(Agent):
    def __init__(self):
        try:
            super().__init__()
            self.chain = self.create_chain(
                {
                    "input_variables": ["user_input"],
                    "template": """
                    The user said: {user_input}
                    """,
                }
            )

        except Exception as e:
            logger.error(f"Error initializing GreetingAgent: {e}")
            raise

    def grade(self, user_input: str):
        try:
            return self.run(self.chain, user_input=user_input)
        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise
