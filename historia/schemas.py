from typing import Optional
from pydantic import BaseModel,Field
from datetime import date, time


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
    historia:Optional[int]
    historiaReferencia:Optional[int]
    idpersona:Optional[int]
    persona:PersonaBase


class HistoriaSquema(BaseModel):
      historia:int = None
      historiaReferencia:Optional[int] 
      persona:PersonaBase =None
      class Config:
        orm_mode = True


class ShowPersona(BaseModel):
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
