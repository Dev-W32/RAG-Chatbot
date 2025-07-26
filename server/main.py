from fastapi import FastAPI

app = FastAPI(title="RAG Chatbot", description="RAG Chatbot API", version="0.0.1")

@app.get("/test")
async def test():
    return  {"message":"test is successful"}