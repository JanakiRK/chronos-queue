from fastapi import FastAPI

app = FastAPI(title="Chronos Task Queue", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to Chronos Task Queue (Python Edition)"}