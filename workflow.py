from agents.generator_agent import GeneratorAgent
from agents.greeting_agent import GreetingAgent
from agents.retrieval_agent import RetrievalAgent

from loguru import logger

from agents.summarization_agent import SummarizationAgent


class WorkFlow:
    def __init__(self):
        self.greeting_agent = GreetingAgent()
        self.retrieve_agent = None
        self.generator_agent = GeneratorAgent()
        self.summarization_agent = SummarizationAgent()

        self.history_window_size = 3
        self.conversation_history = []

    def update_conversation_history(
        self,
        speaker: str,
        conversation_item: str,
    ):
        self.conversation_history.append(speaker + ": " + conversation_item + "\n")
        self.conversation_history = self.conversation_history[-self.history_window_size :]

    def run(self, query: str):

        expertise = self.greeting_agent.greet(query=query)
        print(expertise)
        conversation_summary = self.summarization_agent.summarize(
            query=query, conversation_history=self.conversation_history
        )

        if expertise in ["immigration", "education"]:

            self.retrieve_agent = RetrievalAgent(expertise=expertise)

            search_results = self.retrieve_agent.execute(query=query, top_k=2)
            answer = self.generator_agent.generate_answer(
                expertise=expertise,
                query=query,
                search_results=search_results,
                conversation_history=conversation_summary,
            )

            self.update_conversation_history(speaker="User", conversation_item=query)
            self.update_conversation_history(
                speaker="Bot Assistant", conversation_item=answer
            )
            return answer
        else:
            answer = self.generator_agent.generate_answer(
                expertise=expertise,
                query=query,
                search_results=[],
                conversation_history=conversation_summary,
            )

            self.update_conversation_history(speaker="User", conversation_item=query)
            self.update_conversation_history(
                speaker="Bot Assistant", conversation_item=answer
            )
            return answer


if __name__ == "__main__":
    workflow = WorkFlow()
    query = "I want to study in Toronto. What should we do?"
    result = workflow.run(query=query)
    print(result)
    print("-------------------")
    query = "I want to study in a Cegep in Montreal. What are the requirements?"
    result = workflow.run(query=query)
    print(result)
    print("-------------------")
