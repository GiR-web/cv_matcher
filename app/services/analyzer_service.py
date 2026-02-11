from app.core.embeddings import generate_embedding
from app.core.similarity import calculate_similarity
from app.core.llm import call_llm

def analyze(cv_text: str, job_text: str):
    cv_vec = generate_embedding(cv_text)
    job_vec = generate_embedding(job_text)

    similarity = calculate_similarity(cv_vec, job_vec)

    prompt = f"""
Compare the CV and the job description.
List strengths, gaps and suggestions.
"""

    llm_response = call_llm(prompt)

    return similarity, llm_response
