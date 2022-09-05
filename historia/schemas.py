from typing import Optional
from pydantic import BaseModel,Field
from datetime import date


class PersonaBase(BaseModel):
    id:Optional[int] 
    paterno:str 
    materno:str 
    nombres:str 
    tipoDocumento:int 
    documento:str 
    fechaNacimiento:date 
    genero:int 
    estado:bool = Field(default=True)
    class Config:
        orm_mode = True


class HistoriaBase(BaseModel):
    idpersona:Optional[int]
    historia:Optional[int]
    historiaReferencia:Optional[int]
    class Config:
        orm_mode = True


class CreateHistoria(HistoriaBase):
    persona:PersonaBase
    class Config:
        orm_mode = True


class ViewHistoria(HistoriaBase):
      persona:PersonaBase = None
      class Config:
        orm_mode = True


class ViewPersona(PersonaBase):
    historia:HistoriaBase = None
    class Config:
        orm_mode = True
