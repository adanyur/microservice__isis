from re import I
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, time


class Persona(BaseModel):
    id:int
    paterno:str
    materno:str
    nombres:str
    tipoDocumento:int
    documento:str
    fechaNacimiento:date
    genero:int
    class Config:
        orm_mode = True



class Historia(BaseModel):
    historia:int
    persona:Persona = None
    class Config:
        orm_mode = True


class CitasSquema(BaseModel):
    id:int
    orden:int
    fecha:date
    hora:time
    observacion:str
    paciente:Historia = None
    class Config:
        orm_mode = True


class CitasBase(BaseModel):
    id:Optional[int]
    idprogramacion: int
    historia : int
    orden : int
    fecha : date
    hora: time
    observacion: Optional[str]
    estado: Optional[str] = Field(default='A')



class PlantillaHorariosSquema(BaseModel):
    idprogramacion:int
    orden: int
    fecha:date
    hora: time
    cita:CitasSquema = None
    class Config:
        orm_mode = True



class PlantillaHorariosBase(BaseModel):
    idprogramacion:int
    cupos: int
    minutos:time
    horaInicio:time
    fecha:date



