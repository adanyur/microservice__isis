
from fastapi import Depends,APIRouter, HTTPException
from sqlalchemy import distinct
from models import create_table,Actomedico,Antencedente,Diagnostico
from schemas import ActomedicoOu,ActomedicoIn
from typing import List
from sqlalchemy.orm import Session
from db import get_db,Base


router = APIRouter(prefix='/actomedico',tags=['Actomedico'])

@router.get('/')
def creates_tables():
    create_table()
    return {"message": "create tables"}


@router.get('/listById/{id}',response_model=ActomedicoIn)
def get_byId_actomedico(id:int,db:Session = Depends(get_db)):  
    return db.query(Actomedico).filter(Actomedico.id == id).first();




@router.post('/create')
def create_actomedico(ActomedicoOu:ActomedicoOu,db:Session = Depends(get_db)):
    row_item = Actomedico(**ActomedicoOu.dict(exclude={'antecedentes','diagnosticos','recetas'}))
    db.add(row_item)
    db.commit()
    db.refresh(row_item)
    if row_item:
        create_many_item(db,Antencedente,ActomedicoOu.dict().pop('antecedentes'),'idactomedico',row_item.id)
        create_many_item(db,Diagnostico,ActomedicoOu.dict().pop('diagnosticos'),'idactomedico',row_item.id)
        return {"message":"success"}
    

def create_many_item(db:Session,model:Base,bodys:list,parameters:str,id:int):
    for b in bodys:
        b[parameters] = id
        data = model(**b)
        db.add(data)
        db.commit()
        db.refresh(data)


