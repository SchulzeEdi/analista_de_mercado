from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.phidata_team import PhidataTeam
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

class ChatRequest(BaseModel):
    message: str
    
    class Config:
        arbitrary_types_allowed = True

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

team = PhidataTeam()

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    try:
        if not chat_request.message:
            raise HTTPException(
                status_code=400,
                detail="Mensagem é obrigatória"
            )
        
        print(chat_request)
        content = team.execute_query(chat_request.message)
            
        return {"response": content}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar requisição: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)