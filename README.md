# Log Collector API

API backend desenvolvida em **Flask** para registro e consulta de logs e eventos de aplicações, utilizando **MongoDB** como banco de dados.

O projeto demonstra organização em camadas, validação de dados, tratamento de erros e filtros avançados, com foco em boas práticas de desenvolvimento backend.

---

## Tecnologias

- Python 3.10+
- Flask
- MongoDB
- PyMongo
- python-dotenv

---

## Funcionalidades

- Registro de logs e eventos via API REST
- Estrutura flexível de documentos (metadata dinâmica)
- Filtros por:
  - nível (`level`)
  - serviço (`service`)
  - período (`start_date` / `end_date`)
- Organização em camadas (routes, services, repositories)
- Tratamento adequado de erros
- Healthcheck para monitoramento
- Índices no MongoDB para melhor performance

---

## Estrutura do Projeto

```
log-collector-api/
├── app/
│   ├── config/
│   │   └── settings.py
│   ├── db/
│   │   └── mongo.py
│   ├── repositories/
│   │   └── logs_repository.py
│   ├── routes/
│   │   ├── health_routes.py
│   │   └── logs_routes.py
│   ├── schemas/
│   │   └── log_schema.py
│   ├── services/
│   │   └── logs_service.py
│   ├── utils/
│   │   └── datetime_utils.py
│   └── __init__.py
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

---

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```
MONGO_URI=mongodb://localhost:27017
SECRET_KEY=dev-secret
```

---

## Como executar

1. Criar ambiente virtual (opcional):
```
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate   # Windows
```

2. Instalar dependências:
```
pip install -r requirements.txt
```

3. Executar a aplicação:
```
python run.py
```

A API estará disponível em:
```
http://localhost:5000
```

---

## Endpoints

### Healthcheck

```
GET /health
```

Resposta:
```json
{
  "status": "ok"
}
```

---

### Criar log

```
POST /logs
```

Body (JSON):
```json
{
  "level": "ERROR",
  "service": "auth-service",
  "message": "Token inválido",
  "metadata": {
    "user_id": 123
  }
}
```

Resposta:
```json
{
  "message": "Log criado com sucesso",
  "id": "65a1f9e0e7b8c9d123456789"
}
```

---

### Consultar logs

```
GET /logs
```

Parâmetros opcionais:
- `level`
- `service`
- `start_date` (YYYY-MM-DD)
- `end_date` (YYYY-MM-DD)

Exemplo:
```
GET /logs?level=ERROR&service=auth-service&start_date=2025-12-01&end_date=2025-12-31
```

Resposta:
```json
[
  {
    "id": "65a1f9e0e7b8c9d123456789",
    "level": "ERROR",
    "service": "auth-service",
    "message": "Token inválido",
    "metadata": {
      "user_id": 123
    },
    "created_at": "2025-12-26T13:30:00Z"
  }
]
```

---

## Observações

- O MongoDB é utilizado pela flexibilidade de documentos, ideal para logs.
- Índices são criados automaticamente no startup para melhorar a performance das consultas.
- O projeto foi desenvolvido com foco em clareza, manutenção e boas práticas.

---

## Autor

Gabriel Rubiali  
Computer Science Student | Backend Python
