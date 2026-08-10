from langgraph.graph import START, END, StateGraph

from app.models import State
from app.nodes import classify_intent, retrieve_and_answer, direct_answer


def route(state):
    return state["intent"]

classification = StateGraph(State)
classification.add_node("classify_intent", classify_intent)
classification.add_node("retrieve_and_answer", retrieve_and_answer)
classification.add_node("direct_answer", direct_answer)
classification.add_edge(START, "classify_intent")
classification.add_conditional_edges(
    "classify_intent",
    route,
    {
        "policy_question": "retrieve_and_answer",
        "general_question": "direct_answer",
    },
)
classification.add_edge("retrieve_and_answer", END)
classification.add_edge("direct_answer", END)

graph = classification.compile()
