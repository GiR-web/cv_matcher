from pydantic import BaseModel

class AnalysisInput(BaseModel):
    cv_text: str
    job_text: str

class AnalysisResponse(BaseModel):
    similarity_score: float
    strengths: list[str]
    gaps: list[str]
    suggestions: list[str]
