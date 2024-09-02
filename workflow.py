from agents.generator_agent import GeneratorAgent
from agents.greeting_agent import GreetingAgent
from agents.retrieval_agent import RetrievalAgent

from loguru import logger


class WorkFlow:
    def __init__(self):
        self.greeting_agent = GreetingAgent()
        # output: "immigration", "education", "other" or "not related"

        self.retrieve_agent = None
        self.generator_agent = GeneratorAgent()
        self.conversation_history = ""

    def update_conversation_history(self, query: str):
        self.conversation_history += query
        # self.conversation_history = self.conversation_history[:-1000]
        
    def delete_conversation_history(self):
        self.conversation_history = ""

    def run(self, query: str):
        expertise = self.greeting_agent.greet(
            query=query, conversation_history=self.conversation_history
        )
        self.update_conversation_history(query=query)

        if expertise in ["immigration", "education"]:
            self.retrieve_agent = RetrievalAgent(expertise=expertise)
            search_results = self.retrieve_agent.execute(query=query, top_k=2)
            answer = self.generator_agent.generate_answer(
                expertise=expertise,
                search_results=search_results,
                conversation_history=self.conversation_history,
            )
            return answer
        else:
            answer = self.generator_agent.generate_answer(
                expertise=expertise,
                search_results=[],
                conversation_history=self.conversation_history,
            )
            return answer


if __name__ == "__main__":
    workflow = WorkFlow()
    query="I want to add my spouse to my permanent residence application in Quebec"
    result = workflow.run(query=query)
    print(result)