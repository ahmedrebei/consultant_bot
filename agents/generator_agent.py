from loguru import logger
from agents.agent import Agent


class GeneratorAgent(Agent):
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        try:
            super().__init__(model_name=model_name)
            self.chain = self.create_chain(
                {
                    "input_variables": ["expertise", "search_results", "conversation_history"],
                    "template": """
                    
                    you are a Quebec gouverment assistant with expertise in {expertise}.
                    
                    if expertise is "not related" then generate that the input is not related to Quebec.
                    if expertise is "other" then generate that the input is related to Quebec but I can only help with immigration and education.
                    
                    if expertise is "immigration" or "education" then generate a response based on:
                    - the search results {search_results}.
                    - the conversation history {conversation_history}.
                    """,
                }
            )
        except Exception as e:
            logger.error(f"Error initializing GreetingAgent: {e}")
            raise

    def generate_answer(
        self, expertise: str, search_results: list[str], conversation_history: str
    ) -> str:
        try:
            return self.run(
                self.chain,
                expertise=expertise,
                search_results=search_results,
                conversation_history=conversation_history,
            )
        except Exception as e:
            logger.error(f"Error in GreetingAgent greet: {e}")
            raise
