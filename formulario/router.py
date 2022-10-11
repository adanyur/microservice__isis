from fastapi import Depends,APIRouter, HTTPException
from models import create_table,Formulario,Campos
from schemas import FormularioOut
from typing import List
from sqlalchemy.orm import Session
from db import get_db



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