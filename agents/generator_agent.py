from loguru import logger
from agents.agent import Agent


class GeneratorAgent(Agent):
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        try:
            super().__init__(model_name=model_name)
            self.chain = None

        except Exception as e:
            logger.error(f"Error initializing GreetingAgent: {e}")
            raise

    def generate_prompt(self, expertise: str) -> str:
        try:
            if expertise in ["not related", "other"]:
                return {
                    "input_variables": [
                        "query",
                    ],
                    "template": """
                    You receive the following input query: "{query}".
                    If the expertise is "not related," respond by saying that the input is not related to Quebec and you only help with Quebec related matters.
                    If the expertise is "other," respond by clarifying that you specialize only in immigration or education and cannot assist with other topics.
                    Respond direcly to the query in a clear, concise, and professional manner.
                        
                    Your response:
                    """,
                }

            else:
                return {
                    "input_variables": [
                        "expertise",
                        "query",
                        "search_results",
                        "conversation_history",
                    ],
                    "template": """
                    You are an expert in the domain of {expertise}. You receive the following input query: "{query}".
                    Here are the search results:
                    {search_results}

                    Also, use the summary of the conversation history to maintain continuity and consistency in your responses:
                    {conversation_history}

                    Respond direcly to the query in a clear, concise, and professional manner.
                    
                    Your response:
                    """,
                }

        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise

    def generate_answer(
        self,
        expertise: str,
        query: str,
        search_results: list[str],
        conversation_history: str,
    ) -> str:
        try:
            self.chain = self.create_chain(self.generate_prompt(expertise))

            if expertise in ["not related", "other"]:
                return self.run(self.chain, query=query)
            else:
                return self.run(
                    self.chain,
                    expertise=expertise,
                    query=query,
                    search_results=search_results,
                    conversation_history=conversation_history,
                )
        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise
