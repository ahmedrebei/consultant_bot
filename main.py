from agents.greeting_agent import GreetingAgent


if __name__ == "__main__":
    agent = GreetingAgent()
    response = agent.greet(user_input="I got fired from my job in Vancouver. I want to move to Toronto to study.")
    print(response)