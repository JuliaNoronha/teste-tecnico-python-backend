import datetime
from typing import Optional

from pydantic import BaseModel, Field


class RegistroFocoCreate(BaseModel):
    nivel_foco: int = Field(...,ge=1,le=5)
    tempo_minutos: int
    comentario: str
    categoria: Optional[str] = "Geral"
    data: datetime = Field(default_factory=datetime.now)

class RegistroFocoResponse(RegistroFocoCreate):
    id: int

    class Config:
        from_attributes = True