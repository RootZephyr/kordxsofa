from fastapi import FastAPI

app = FastAPI(title="SofaScore API")

@app.get("/")
def root():
    return {"status": "ok", "message": "SofaScore API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
