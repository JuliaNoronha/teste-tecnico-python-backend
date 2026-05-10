from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Api de Foco e Produtividade")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/registro-foco", response_model=schemas.RegistroFocoResponse)
def criar_registro(registro: schemas.RegistroFocoCreate, db: Session = Depends(get_db())):
    novo_registro = models.RegistroFocoModel(
        nivel_foco=registro.nivel_foco,
        tempo_minutos=registro.tempo_minutos,
        comentario=registro.comentario,
        categoria=registro.categoria,
        data=registro.data
    )

    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)

    return novo_registro
