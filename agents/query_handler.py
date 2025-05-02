from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm=Ollama(model="llama3.2")

query_prompt = PromptTemplate.from_template("""
You are an expert assistant. Answer this question based on the simplified policy content:

Question: "{query}"

Simplified Policy:
"{simplified_text}"
""")

query_chain = LLMChain(llm=llm, prompt=query_prompt)

def run(state):
    response = query_chain.run(
        query=state["query"],
        simplified_text=state["simplified_text"]
    )
    return {**state, "answer": response}
