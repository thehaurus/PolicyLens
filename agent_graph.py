from langgraph.graph import StateGraph
from typing import TypedDict
from agents import document_parser, simplifier, query_handler, personalizer, feedback_collector

class AgentState(TypedDict, total=False):
    pdf: object
    query: str
    raw_text: str
    simplified_text: str
    answer: str
    Explanation: str
    Personalized_Tip: str
    Relevant_Clause: str
    profile: dict  # <-- Add this

def personalized_node(state):
    print(f"state ==> {state}")
    return personalizer.run(state, state["profile"])


def run_policy_assistant(pdf_file, user_query, profile):
    
    workflow = StateGraph(state_schema=AgentState)

    # Add agent nodes
    workflow.add_node("parse", document_parser.run)
    workflow.add_node("simplify", simplifier.run)
    workflow.add_node("handle_query", query_handler.run)
    workflow.add_node("personalize", personalized_node)
    workflow.add_node("feedback", feedback_collector.run)

    # Graph structure
    workflow.set_entry_point("parse")
    workflow.add_edge("parse", "simplify")
    workflow.add_edge("simplify", "handle_query")
    workflow.add_edge("handle_query", "personalize")
    workflow.add_edge("personalize", "feedback")

    # Compile & run
    graph = workflow.compile()
    return graph.invoke({
    "pdf": pdf_file,
    "query": user_query,
    "profile": profile
})




# pdf_file = "examples/Sample_Policy.pdf"
# user_query = "What are Termination Rights of the Policyholder"
# profile = {
#   "age": 45,
#   "location": "Rhode Island",
#   "plan": "Standard"
# }
# print(run_policy_assistant(pdf_file, user_query, profile))