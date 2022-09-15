from typing import Optional,List
from pydantic import BaseModel,Field
from datetime import date, time


class Cie10Base(BaseModel):
    id:Optional[int]
    codigo:Optional[str]
    descripcion:Optional[str]
    estado:Optional[bool]

class AntecedenteBase(BaseModel):
    idactomedico:Optional[int]
    idantecedente:int
    descripcion:str
 
class RecetaBase(BaseModel):
    id:Optional[int]
    idactomedico:Optional[int]

class DiagnosticoBase(BaseModel):
    id:Optional[int]
    idactomedico:Optional[int]
    idcie10:int
    tipodiagnostico:int

class ActomedicoBase(BaseModel):
    id:Optional[int]
    idadmision:int
    motivoconsulta:str
    enferproblemaactual:str
    examenfisico:str
    presionarterial:float
    cardiaca:float
    respiratoria:float
    tempbucal:float
    tempaxilar:float
    peso:float
    talla:float
    masacorporal:float
    perimcefalico:float
    atencion:int


class Cie10In(Cie10Base):
    class Config:
        orm_mode = True

class ActomedicoIn(ActomedicoBase):
    idcita:Optional[int]
    antecedentes:List[AntecedenteBase] = None
    recetas:List[RecetaBase] = None
    diagnosticos:List[DiagnosticoBase] = None

#
class AntecedenteIn(AntecedenteBase):
    class Config:
        orm_mode = True
    
class DiagnosticoIn(DiagnosticoBase):
    cie10:Cie10In = None
    class Config:
        orm_mode = True


class ActomedicoOu(ActomedicoBase):
    antecedentes:List[AntecedenteIn] = None
    diagnosticos:List[DiagnosticoIn] = None
    class Config:
        orm_mode = True