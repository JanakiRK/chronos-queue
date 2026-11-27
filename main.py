from fastapi import FastAPI, HTTPException
from database import get_db_connection

app = FastAPI(title="Chronos Task Queue", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to Chronos Task Queue (Python Edition)"}

@app.get("/health/db")
def check_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"status": "success", "postgresql_version": db_version["version"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))