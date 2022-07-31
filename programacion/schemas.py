from typing import Optional
from pydantic import BaseModel
from datetime import date, time


class MedicosModel(BaseModel):
    id:int
    class Config:
        orm_mode = True

class ConsultoriosModel(BaseModel):
    id:int
    class Config:
        orm_mode = True

class EspecialidadesModel(BaseModel):
    id:int
    descripcion:str
    class Config:
        orm_mode = True

class TurnosModel(BaseModel):
    id:int
    class Config:
        orm_mode = True

class ProgramacionBase(BaseModel):
    id:Optional[int]
    idmedico:int
    idconsultorio:int
    idespecialidad:int
    idturno:int
    fecha:date
    estado:str
    cupos:int
    minutos:time
    observacion:str


class ProgramacionSchema(BaseModel):
    id:int
    fecha:date 
    estado:str 
    cupos:int  
    minutos:time 
    observacion:str 
    especialidad:EspecialidadesModel = None 
    medico:MedicosModel = None 
    consultorio:ConsultoriosModel = None 
    turno:TurnosModel = None 

    class Config:
        orm_mode = True
