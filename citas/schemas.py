from re import I
from typing import Optional
from pydantic import BaseModel
from datetime import date, time



class CitasBase(BaseModel):
    idprogramacion: int
    historia : int
    orden : int
    fecha : date
    hora: time
    observacion: str
    estado: str

