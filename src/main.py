from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
import uuid
from typing import Optional

# Pydantic models
class AnalyzePRRequest(BaseModel):
    repo_url: str
    pr_number: int
    github_token: Optional[str] = None

# FastAPI app initialization
app = FastAPI()

# Error Handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "body": exc.body}
    )

# Routes
@app.post("/analyze-pr")
async def analyze_pr(data: AnalyzePRRequest):
    return {
            "repo_url": data.repo_url,
            "pr_number": data.pr_number,
            "github_token": data.github_token
        }
    