# 🚀 API de Foco e Produtividade

Este projeto é uma API desenvolvida com **FastAPI** para ajudar desenvolvedores e estudantes a registrarem e analisarem sua produtividade através de sessões de foco.

## Tecnologia

- **Python 3.9+**
- **FastAPI** (Framework web)
- **SQLAlchemy** (ORM para banco de dados)
- **SQLite** (Banco de dados Local)

## Como rodar o projeto

### 1. Clonar o repositório

```bash

git clone [URL_DO_SEU_REPOSITORIO]
cd teste-tecnico-python-backend
```

### 2. Criar ambiente virtual 

``` 
python -m venv venv
# No windows:
  venv\Scripts\activate
# No Linux/Mac:
  source venv/bin/activate
```

### 3. Instalar dependências
``` bash
  pip install -r requirements.txt
```

### 4. Executar a API
```bash
  uvicorn main:app --reload
```

#### A API estará disponível em ```http://127.0.0.1:8000```.

## Como testar

### O FastAPI gera uma documentação interativa automática. Para testar os endpoints:

#### 1. Acesse: http://127.0.0.1:8000/docs
#### 2. Utilize o botão "Try it out" no endpoint ```POST /registro-foco``` para enviar dados.
#### 3. Utilize o endpoint ``` GET /diagnostico-produtividade``` para ver sua média e o feedback inteligente.
