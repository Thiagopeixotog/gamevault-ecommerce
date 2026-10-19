from fastapi import FastAPI

app = FastAPI(title="GameVault API", version="0.1.0")

@app.get("/")
def root():
    return {"message": "GameVault API is running"}

