from pydantic import BaseModel
from typing import List

class RequestSchema(BaseModel):
    query: str

class ResponseSchema(BaseModel):
    answer: str
    sources: List[str]
    confidence: float
