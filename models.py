import datetime
from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class RegistroFocoModel(Base):
    __tablename__: "registros_foco"

    id = Column(Integer, primary_key=True, index=True)
    nivel_foco = Column(Integer)
    tempo_minutos = Column(Integer)
    comentario = Column(String)
    categoria = Column(String, default="Geral")
    data = Column(DateTime, default=datetime.now)
