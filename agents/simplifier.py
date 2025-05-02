from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm=Ollama(model="llama3.2")

simplify_prompt = PromptTemplate.from_template("""
You are a legal document simplifier. Simplify the following insurance policy text into plain English:
"{raw_text}"
""")

simplify_chain = LLMChain(llm=llm, prompt=simplify_prompt)

def run(state):
    raw_text = state["raw_text"]
    simplified_text = simplify_chain.run(raw_text=raw_text)
    return {**state, "simplified_text": simplified_text}
