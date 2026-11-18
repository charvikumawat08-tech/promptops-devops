# PromptOps LLM Prompt Versioning API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="PromptOps Versioning API")

# In-memory list storing prompt versions (no database needed)
prompts = [
    {"version": 1, "text": "You are a helpful customer support assistant.", "status": "active"}
]

class PromptInput(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/prompts")
def get_all_prompts():
    return {"prompts": prompts}

@app.get("/prompts/active")
def get_active_prompt():
    for p in reversed(prompts):
        if p["status"] == "active":
            return p
    raise HTTPException(status_code=404, detail="No active prompt found")

@app.post("/prompts")
def add_prompt(item: PromptInput):
    for p in prompts:
        if p["status"] == "active":
            p["status"] = "previous"
    new_version = len(prompts) + 1
    new_prompt = {"version": new_version, "text": item.text, "status": "active"}
    prompts.append(new_prompt)
    return new_prompt