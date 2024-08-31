from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from loguru import logger

from config import OPENAI_API_KEY



class Agent:
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        try:
            self.llm = ChatOpenAI(model=model_name, api_key=OPENAI_API_KEY, max_tokens=1000, temperature=0.5)
        except Exception as e:
            logger.error(f"Error initializing OpenAI model: {e}")
            raise
    def create_chain(self, template: str):
        try:
            prompt_template = PromptTemplate(
                input_variables=template["input_variables"],
                template=template["template"],
            )
            return LLMChain(llm=self.llm, prompt=prompt_template)
        except Exception as e:
            logger.error(f"Error creating LLMChain: {e}")
            raise
    def run(self, chain, **kwargs) -> str:
        try:
            return chain.run(**kwargs)
        except Exception as e:
            logger.error(f"Error running LLMChain: {e}")
            raise
