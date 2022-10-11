from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, time


#BASE
class EspecialidadBase(BaseModel):
    id:Optional[int]
    descripcion:Optional[str]

class MedicoBase(BaseModel):
    id:Optional[int]
    descripcion:Optional[str]

class ConsultorioBase(BaseModel):
    id:Optional[int]
    descripcion:Optional[str]

class TurnoBase(BaseModel):
    id:Optional[int]
    descripcion:Optional[str]

class MedicoBase(BaseModel):
    id:Optional[int]
    nombres:Optional[str]

class CoberturaBase(BaseModel):
    id:Optional[int]
    codigo:str
    subcobertura:str
    descripcion:str


class PlantillaHorariosBase(BaseModel):
    idprogramacion:Optional[int]
    cupos: Optional[int]
    minutos:Optional[time]
    horaInicio:Optional[time]
    fecha:Optional[date]

class CitasBase(BaseModel):
    id:Optional[int]
    idprogramacion:int
    orden : Optional[int]
    fecha : Optional[date]
    hora: Optional[time]
    observacion: Optional[str]
    estado: str = Field(default='R')

class CreateCita(CitasBase):
    idprogramacion:int
    historia:int

class updateCita(BaseModel):
    idcita:int
    estado:str


class ProgramacionBase(BaseModel):
    id:Optional[int]
    fecha:Optional[date]
    estado:Optional[str]
    cupos:Optional[int]
    minutos:Optional[time]
    observacion:Optional[str]


class PersonaBase(BaseModel):
    id:Optional[int]
    paterno:Optional[str]
    materno:Optional[str]
    nombres:Optional[str]
    tipodocumento:Optional[int]
    documento:Optional[str]
    fechanacimiento:Optional[date]
    genero:Optional[int]

class HistoriaBase(BaseModel):
     historia:Optional[int]


class AdmisionBase(BaseModel):
    id:Optional[int]
    idcita:Optional[int]
    acreditacion:Optional[str]
    idcobertura:Optional[int]
    copagofijo:Optional[str]
    copagovariable:Optional[str]
    numeroautorizacion:Optional[str]
    fincarencia:Optional[str]
