from fastapi import FastAPI
import uvicorn
from chatbot import taxation_chatbot

app = FastAPI()

@app.get("/tax_chatbot")
def chat(query: str):
    response = taxation_chatbot(query)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)