from typing import Optional
from pydantic import BaseModel,Field
from datetime import date, time



class AdmisionBase(BaseModel):
    id:Optional[int]
    idcita:int
    # idacreditacion:int
    idcobertura:Optional[int]
    # idatencion:int
    # idtipocuenta :int
    observacion:str
    copagofijo:Optional[str]
    copagovariable:Optional[str]
    numeroautorizacion:Optional[str]
    fincarencia:Optional[str]
    estado : bool = Field(default=True)