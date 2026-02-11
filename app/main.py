# app/main.py
from fastapi import FastAPI
from app.api.routes import router  # importa o roteador do routes.py

# Cria a aplicação FastAPI
app = FastAPI(
    title="GenAI CV Matcher",
    description="API para comparação semântica de currículos e vagas usando GenAI open-source",
    version="0.1.0"
)

# Inclui o roteador com todos os endpoints do routes.py
app.include_router(router)
