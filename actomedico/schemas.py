from typing import Optional,List
from pydantic import BaseModel,Field
from datetime import date, time



class AntecedenteBase(BaseModel):
    id:Optional[int]
    idactomedico:Optional[int]
    idantecedente:int
    descripcion:str
 
class RecetaBase(BaseModel):
    id:Optional[int]
    idactomedico:Optional[int]

class DiagnosticoBase(BaseModel):
    id:Optional[int]
    idactomedico:Optional[int]
    idciex:str
    tipodiagnostico:int

class ActomedicoBase(BaseModel):
    id:Optional[int]
    idadminsion:int
    motivoconsulta:str
    enferproblemaactual:str
    examenfisico:str
    presionarterial:int
    cardiaca:int
    respiratoria:int
    tempbucal:int
    tempaxilar:int
    peso:int
    talla:int
    masacorporal:Optional[int]
    perimcefalico:int
    atencion:Optional[str]



class ActomedicoOu(ActomedicoBase):
    antecedentes:List[AntecedenteBase] = None
    recetas:List[RecetaBase] = None
    diagnosticos:List[DiagnosticoBase] = None



#
class AntecedenteIn(AntecedenteBase):
    class Config:
        orm_mode = True
    
class DiagnosticoIn(DiagnosticoBase):
    class Config:
        orm_mode = True




class ActomedicoIn(ActomedicoBase):
    antecedentes:List[AntecedenteIn] = None
    diagnosticos:List[DiagnosticoIn] = None
    class Config:
        orm_mode = True