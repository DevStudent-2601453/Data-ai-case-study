from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.schemas import ResponseSchema
from app.graph import graph


class AskRequest(BaseModel):
    query: str


app = FastAPI(title="Zepto Support Assistant")


@app.post("/ask", response_model=ResponseSchema)
def ask(req: AskRequest):
    state = {"question": req.query}
    try:
        result = graph.invoke(state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    try:
        response = ResponseSchema(**{
            "answer": result.get("answer", ""),
            "sources": result.get("sources", []),
            "confidence": float(result.get("confidence", 0.0)),
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid response schema: {e}")

    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=7860, reload=False)
