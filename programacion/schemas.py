from datetime import date, time
from typing import Optional

from base import *
from pydantic import BaseModel, Field


class ProgramacionParameters(BaseModel):
    fecha:date
    especialidad:int


class MedicosModel(MedicoBase):
    class Config:
        orm_mode = True

class ConsultoriosModel(ConsultoriosBase):
    class Config:
        orm_mode = True

class EspecialidadesModel(EspecialidadesBase):
    class Config:
        orm_mode = True

class TurnosModel(TurnoBase):
    class Config:
        orm_mode = True

class ProgramacionSchema(ProgramacionBase):
    especialidad:EspecialidadesModel = None 
    medico:MedicosModel = None 
    consultorio:ConsultoriosModel = None 
    turno:TurnosModel = None 
    class Config:
        orm_mode = True

class ProgramacionEspecialidadesEsquema(BaseModel):
    especialidad:EspecialidadesModel = None
    class Config:
        orm_mode = True


class UpdateProgramacion(BaseModel):
    idprogramacion:int
    esatdo:str