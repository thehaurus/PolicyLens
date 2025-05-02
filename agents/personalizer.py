from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm=Ollama(model="llama3.2")

personalize_prompt = PromptTemplate.from_template("""
You're a personalized insurance assistant.

Given:
- Answer: {answer}
- User Profile: Age {age}, Location {location}, Plan {plan}

Rewrite the answer in a personalized and empathetic tone. Also, suggest any helpful tips or mention related clauses.
""")

personalize_chain = LLMChain(llm=llm, prompt=personalize_prompt)

def run(state, profile):
    result = personalize_chain.run(
        answer=state["answer"],
        age=str(profile["age"]),
        location=profile["location"],
        plan=profile["plan"]
    )
    return {
        **state,
        "Explanation": state["answer"],
        "Personalized_Tip": result,
    }

