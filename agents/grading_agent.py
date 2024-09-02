from loguru import logger
from agents.agent import Agent


class GradingAgent(Agent):
    def __init__(self, expertise: str, model_name: str = "gpt-3.5-turbo"):
        try:
            super().__init__(model_name=model_name)
            self.expertise = expertise
            self.chain = self.create_chain(
                {
                    "input_variables": ["query", "retrieved_data", "expertise"],
                    "template": """
                    you are an expert in {expertise} for the gouvernement of Quebec.
                    given the following user input: {query}, evaluate if the retrieved data :{retrieved_data} is relevant. 
                    output: "true" or "false"
                    don't give any natural language output here, just the evaluation.
                    """,
                }
            )

        except Exception as e:
            logger.error(f"Error initializing GreetingAgent: {e}")
            raise

    def grade(self, query: str, retrieved_data: str):
        """grade the retrieved data based on the user input

        Args:
            query (str): user query
            retrieved_data (str): retrieved data

        Returns:
            str: "true" or "false"
        """
        try:
            return self.run(
                self.chain,
                query=query,
                retrieved_data=retrieved_data,
                expertise=self.expertise,
            )
        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise
