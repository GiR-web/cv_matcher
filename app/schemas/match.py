from pydantic import BaseModel
from typing import List

class MatchRequest(BaseModel):
    cv_text: str
    job_text: str

class MatchResponse(BaseModel):
    similarity_score: float
    strengths: List[str] = []
    gaps: List[str] = []
    suggestions: List[str] = []
