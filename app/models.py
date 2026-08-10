from typing import TypedDict

class State(TypedDict, total=False):
    question: str
    intent: str
    answer: str
    sources: list[str]
    confidence: float
