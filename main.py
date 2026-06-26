from fastapi import FastAPI
from schemas import EchoRequest, EchoResponse

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/echo", response_model=EchoResponse)
def echo(request: EchoRequest):
    return {"message": request.message}