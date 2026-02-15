# CV Matcher API

API desenvolvida com **FastAPI** para avaliar a compatibilidade entre um currículo e uma descrição de vaga por meio de **similaridade semântica de texto**.

O sistema utiliza técnicas de **Processamento de Linguagem Natural (NLP)** para transformar os textos em embeddings numéricos e calcular o grau de correspondência entre eles usando **cosine similarity**.

O projeto demonstra uma aplicação prática de modelos de linguagem para **análise de significado**, sem uso de modelos generativos, fine-tuning ou persistência de dados.

## Principais características
- Geração de embeddings com **Sentence Transformers**
- Cálculo de similaridade semântica entre CV e vaga
- Extração básica de habilidades (skills)
- API REST documentada via **Swagger / OpenAPI**
- Arquitetura simples, modular e orientada a serviços
