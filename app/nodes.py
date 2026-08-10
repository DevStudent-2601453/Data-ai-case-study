import os
from dotenv import load_dotenv
from pydantic import ValidationError
from app.retriever import retrieve
from app.prompt import build_prompt, build_general_prompt
from app.schemas import ResponseSchema

load_dotenv()
mock_llm = os.getenv("MOCK_LLM", "1")

groq_client = None
if mock_llm == "0":
    try:
        from groq import Groq

        groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    except Exception:
        groq_client = None


intent_classifier_prompt = """
You are an intent classifier.

Classify the user's question into exactly one of these categories:

1. policy_question
   - Questions about delivery
   - Returns
   - Refunds
   - Membership
   - Order tracking
   - Order cancellation
   - Gift cards
   - Support hours

2. general_question
   - Any question not related to the above topics.

Return exactly one label and nothing else.

Allowed labels:
- policy_question
- general_question

Do not provide any explanation.

Example:
Question: Where is my delivery?
Label: policy_question

Question: Tell me a joke.
Label: general_question
"""


def classify_intent(state):
    question = state["question"]
    lower_question = question.lower()
    keywords = ["delivery", "return", "refund", "membership", "tracking", "cancel", "gift card", "support hours"]

    if mock_llm == "1":
        if any(keyword in lower_question for keyword in keywords):
            state["intent"] = "policy_question"
        else:
            state["intent"] = "general_question"
        return state

    elif mock_llm == "0":
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": intent_classifier_prompt},
                {"role": "user", "content": question},
            ],
            temperature=0,
        )
        label = response.choices[0].message.content.strip()
        if label not in ["policy_question", "general_question"]:
            label = "general_question"
        state["intent"] = label
        return state

    else:
        raise ValueError(f"Invalid MOCK_LLM value: {mock_llm}. Expected '0' or '1'.")


def retrieve_and_answer(state):
    question = state["question"]
    retrieved_documents = retrieve(question, top_k=3)
    documents = retrieved_documents["documents"]
    sources = retrieved_documents["ids"]

    if mock_llm == "1":
        top_chunk = documents[0]
        top_chunk_snippet = top_chunk[:200]
        state["answer"] = f"Based on the retrieved context:\n\n{top_chunk_snippet}"
        state["sources"] = sources
        state["confidence"] = 1.0
        return state

    elif mock_llm == "0":
        context = "\n\n".join(documents)
        rag_prompt = build_prompt(context=context, question=question)
        for attempt in range(3):
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": rag_prompt}],
                    temperature=0.2,
                )
                raw_output = response.choices[0].message.content.strip()
                validated = ResponseSchema.model_validate_json(raw_output)
                state["answer"] = validated.answer
                state["sources"] = sources
                state["confidence"] = validated.confidence
                return state
            except ValidationError:
                if attempt < 2:
                    rag_prompt += "\nYour previous response was not valid JSON. Return ONLY valid JSON matching the required schema."
        state["answer"] = "ERROR: Failed to generate valid JSON."
        state["sources"] = []
        state["confidence"] = 0.0
        return state

    else:
        raise ValueError(f"Invalid MOCK_LLM value: {mock_llm}. Expected '0' or '1'.")


def direct_answer(state):
    if mock_llm == "1":
        state["answer"] = "I can only answer questions about Zepto policies right now."
        state["sources"] = []
        state["confidence"] = 1.0
        return state

    elif mock_llm == "0":
        prompt = build_general_prompt(question=state["question"])
        for attempt in range(3):
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                )
                raw_output = response.choices[0].message.content.strip()
                validated = ResponseSchema.model_validate_json(raw_output)
                state["answer"] = validated.answer
                state["sources"] = []
                state["confidence"] = validated.confidence
                return state
            except ValidationError:
                if attempt < 2:
                    prompt += "\nYour previous response was not valid JSON. Return ONLY valid JSON matching exactly this schema: {\"answer\": \"...\", \"sources\": [], \"confidence\": 0.95}."
        state["answer"] = "ERROR: Failed to generate valid JSON."
        state["sources"] = []
        state["confidence"] = 0.0
        return state

    else:
        raise ValueError(f"Invalid MOCK_LLM value: {mock_llm}. Expected '0' or '1'.")
