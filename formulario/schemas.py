from typing import List, Optional

from pydantic import BaseModel, Field


class FormularioBase(BaseModel):
    id:Optional[int]
    descripcion:Optional[str]
    estado:bool = Field(default=True)


class CamposBase(BaseModel):
    id:Optional[int]
    idformulario:Optional[int]
    label:Optional[str]
    controltype:Optional[str]
    type:Optional[str]
    order:Optional[int]
    value:Optional[str]
    


class CamposOut(CamposBase):
    class Config:
        orm_mode = True    

class FormularioOut(FormularioBase):
    campos:List[CamposOut]
    class Config:
        orm_mode = True