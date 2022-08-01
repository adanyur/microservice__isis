from typing import Optional
from pydantic import BaseModel
from datetime import date, time


class MedicosModel(BaseModel):
    id:int
    idespecialidad:int
    nombres:str
    intervalo:time
    class Config:
        orm_mode = True

class ConsultoriosModel(BaseModel):
    id:int
    descripcion:str
    class Config:
        orm_mode = True

class EspecialidadesModel(BaseModel):
    id:int
    descripcion:str
    class Config:
        orm_mode = True

class TurnosModel(BaseModel):
    id:int
    descripcion:str
    horainicio:time
    horafin:time
    horas:time
    class Config:
        orm_mode = True

class ProgramacionBase(BaseModel):
    id:Optional[int]
    idmedico:int
    idconsultorio:int
    idespecialidad:int
    idturno:int
    fecha:date
    estado:Optional[str]
    cupos:Optional[int]
    minutos:Optional[time]
    observacion:Optional[str]


class ProgramacionSchema(BaseModel):
    id:int
    fecha:date
    estado:str = None
    cupos:int   = None
    minutos:time  = None
    observacion:str = None
    idconsultorio:int
    idespecialidad:int
    idturno:int
    idmedico:int
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


class ProgramacionMedicosEsquema(BaseModel):
    id:int
    cupos:int   = None
    minutos:time  = None
    idespecialidad:int
    medico:MedicosModel
    class Config:
        orm_mode = True