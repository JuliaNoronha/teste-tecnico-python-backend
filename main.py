from aiohttp.web_exceptions import HTTPException
from fastapi import FastAPI
from fastapi.params import Depends
from pkg_resources import resource_filename
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
def criar_registro(registro: schemas.RegistroFocoCreate, db: Session = Depends(get_db)):
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

@app.get("/diagnostico-produtividade")
def obter_diagnostico(db: Session = Depends(get_db)):
    registros = db.query(models.RegistroFocoModel).all()

    if not registros:
        raise HTTPException(status_code=404, detail="Nenhum registro encontrado para análise.")

    total_minutos = sum(r.tempo_minutos for r in registros)
    media_foco = sum(r.nivel_foco for r in registros) / len(registros)

    if media_foco >= 4:
        feedback = "Você está muito produtivo. Parabéns!"
    elif media_foco >= 3:
        feedback = "Está indo bem, mas podemos melhorar, não acha?"
    else:
        feedback = "Faça pausas mais longas, porém longe de redes sociais, por favor."

    return {
        "media_nivel_foco": round(media_foco,2),
        "tempo_total_focado_minutos": total_minutos,
        "total_sessoes": len(registros),
        "diagnostico": feedback
    }