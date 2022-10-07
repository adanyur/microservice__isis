from typing import Optional
from pydantic import BaseModel,Field
from datetime import date, time



class AdmisionBase(BaseModel):
    id:Optional[int]
    idcita:int
    acreditacion:str
    idcobertura:Optional[int]
    copagofijo:Optional[str]
    copagovariable:Optional[str]
    numeroautorizacion:Optional[str]
    fincarencia:Optional[str]
    observacion:str = Field(default=None)
    estado : bool = Field(default=True)