# CV Matcher API

API desenvolvida com **FastAPI** para avaliar a compatibilidade entre um currículo e uma descrição de vaga por meio de **similaridade semântica de texto**.

O sistema utiliza técnicas de **Processamento de Linguagem Natural (NLP)** para gerar embeddings dos textos com **Sentence Transformers** e calcular o grau de correspondência usando **cosine similarity**.

O projeto demonstra uma aplicação prática de **análise semântica**, sem uso de modelos generativos, APIs comerciais ou fine-tuning.

## Principais características
- Geração de embeddings com Sentence Transformers (MiniLM)
- Cálculo de similaridade semântica entre CV e vaga
- Extração básica de habilidades via palavras-chave
- Geração de strengths, gaps e sugestões
- API REST documentada automaticamente via Swagger (OpenAPI)
- Arquitetura simples e modular com FastAPI


