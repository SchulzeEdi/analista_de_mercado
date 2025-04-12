from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.phidata_team import PhidataTeam
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Analista de Mercado API",
    description="API para análise do mercado financeiro",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        team = PhidataTeam()
        response = team.execute_query(request.message)
        return ChatResponse(response=response)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)