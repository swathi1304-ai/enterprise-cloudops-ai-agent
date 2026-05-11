from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {
        "message": "Enterprise CloudOps AI Agent is running",
        "status": "healthy",
        "timestamp": str(datetime.now())
    }

@app.post("/ask")
def ask_ai(request: PromptRequest):
    return {
        "question": request.prompt,
        "response": f"AI processed: {request.prompt}",
        "status": "success"
    }

@app.post("/generate-terraform")
def generate_terraform(request: PromptRequest):

    terraform_code = f'''
resource "google_storage_bucket" "demo_bucket" {{
  name     = "enterprise-ai-demo"
  location = "US"
}}
'''

    return {
        "prompt": request.prompt,
        "terraform": terraform_code,
        "status": "generated"
    }
