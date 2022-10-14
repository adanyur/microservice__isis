from typing import List

from db import get_db
from fastapi import APIRouter, Depends
from models import Campos, Formulario, create_table
from schemas import FormularioOut
from sqlalchemy.orm import Session

router = APIRouter(prefix='/formulario',tags=['Formulario'])

@router.get('/createTable')
def creates_tables():
    create_table()    
    return;


@router.get('/listado',response_model=List[FormularioOut])
async def listado_formulario(db:Session = Depends(get_db)):
    return  db.query(Formulario).all()



@router.get('/listado/{id}',response_model=FormularioOut)
async def get_formulario(id:int,db:Session = Depends(get_db)):
    return db.query(Formulario).filter(Formulario.id == id,Formulario.estado == True).first()