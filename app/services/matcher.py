# app/services/matcher.py
import re
from sentence_transformers import SentenceTransformer, util

# Carrega o modelo uma vez só
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Lista inicial de skills comuns (você pode expandir)
COMMON_SKILLS = [
    "python", "fastapi", "docker", "sql", "postgresql", "ci/cd",
    "git", "unit testing", "aws", "machine learning", "nlp",
    "javascript", "react", "docker-compose", "pandas", "numpy"
]

def extract_skills(text: str) -> set:
    """
    Extrai skills de um texto baseado em palavras-chave conhecidas.
    """
    text_lower = text.lower()
    skills_found = {skill for skill in COMMON_SKILLS if skill in text_lower}
    return skills_found

def match_texts(cv_text: str, job_text: str) -> dict:
    """
    Compara semanticamente CV x Job usando embeddings.
    Retorna um dict com similarity_score, strengths, gaps e sugestões.
    """

    # 1️⃣ Cria embeddings
    embeddings = model.encode([cv_text, job_text], convert_to_tensor=True)
    similarity_score = float(util.cos_sim(embeddings[0], embeddings[1]).item())
    similarity_score = round(similarity_score, 2)

    # 2️⃣ Extrai skills
    cv_skills = extract_skills(cv_text)
    job_skills = extract_skills(job_text)

    # 3️⃣ Determina forças e gaps
    strengths = list(cv_skills & job_skills)  # habilidades em comum
    gaps = list(job_skills - cv_skills)       # habilidades que faltam

    # 4️⃣ Sugestões baseadas nos gaps (máx 5)
    suggestions = [f"Consider adding '{gap}' to your CV." for gap in gaps[:5]]

    # 5️⃣ Resultado final
    result = {
        "similarity_score": similarity_score,
        "strengths": strengths,
        "gaps": gaps,
        "suggestions": suggestions
    }

    # ✅ Debug no terminal
    print(result)

    return result
