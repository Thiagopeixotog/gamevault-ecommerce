from fastapi import FastAPI

app = FastAPI(title="Joystock API", version="0.1.0")

@app.get("/")
def root():
    return {"message": "Joystock API is running"}

