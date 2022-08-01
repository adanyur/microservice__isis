from typing import Optional
from pydantic import BaseModel
from datetime import date, time


class EspecialidadesBase(BaseModel):
    id:int = None
    descripcion:str = None
    class Config:
        orm_mode = True

class TurnosBase(BaseModel):
    id:int
    descripcion:str
    horainicio:time
    horafin:time
    horas:time
    class Config:
        orm_mode = True

class MedicosBase(BaseModel):
    id:int
    idespecialidad:int
    nombres:str
    intervalo:time
    class Config:
        orm_mode = True

class ConsultoriosBase(BaseModel):
    id:int
    descripcion:str
    class Config:
        orm_mode = True