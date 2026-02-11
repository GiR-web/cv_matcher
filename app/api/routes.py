# app/api/routes.py
from fastapi import APIRouter
from app.services.matcher import match_texts
from app.schemas.match import MatchRequest, MatchResponse

# Cria o roteador do FastAPI
router = APIRouter()

# Endpoint para analisar CV x Job
@router.post("/analyze", response_model=MatchResponse)
def analyze_cv(data: MatchRequest):
    """
    Recebe o texto do CV e da vaga, chama o matcher e retorna:
    - similarity_score (float)
    - strengths (list)
    - gaps (list)
    - suggestions (list)
    """
    # Chama o matcher e recebe o dict com todos os campos
    result = match_texts(data.cv_text, data.job_text)

    # Retorna os valores separados para o Pydantic
    return MatchResponse(
        similarity_score=result["similarity_score"],
        strengths=result["strengths"],
        gaps=result["gaps"],
        suggestions=result["suggestions"]
    )



