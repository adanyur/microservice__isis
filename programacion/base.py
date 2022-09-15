from typing import Optional
from pydantic import BaseModel,Field
from datetime import date, time

class MedicoBase(BaseModel):
    id:int
    idespecialidad:int
    nombres:str
    intervalo:time

class ConsultoriosBase(BaseModel):
    id:int
    descripcion:str

class EspecialidadesBase(BaseModel):
    id:int
    descripcion:str

class TurnoBase(BaseModel):
    id:int
    descripcion:str
    horainicio:time
    horafin:time
    horas:time


class ProgramacionBase(BaseModel):
    id:Optional[int]
    idconsultorio:int
    idespecialidad:int
    fecha:date
    minutos:Optional[time]
    estado:str = Field(default='A')
    cupos:Optional[int]
    observacion:Optional[str]


class ProgramacionIn(ProgramacionBase):
    medico:MedicoBase = None
    turno:TurnoBase = None
    