from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI()

# health check
@app.get("/")
def health():
    return {"status": "ok"}

# endpoint for uploading: /upload
app.include_router(upload_router, prefix="/upload")
