from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot.responses import post_investment_response

class Message(BaseModel):
    message: str

app = FastAPI()

# CORS setup for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  #

@app.post("/chat")
async def chat(msg: Message):
    response = post_investment_response(msg.message)
    return {"response": response}

@app.get("/")
def health():
    return {"status": "ok"}