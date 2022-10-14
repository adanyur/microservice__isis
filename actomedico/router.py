
from typing import List

from db import Base, get_db
from fastapi import APIRouter, Depends, HTTPException
from models import Actomedico, Antencedente, Cita, Diagnostico, create_table
from schemas import ActomedicoIn, ActomedicoOu
from sqlalchemy import distinct
from sqlalchemy.orm import Session

router = APIRouter(prefix='/actomedico',tags=['Actomedico'])

@router.get('/')
def creates_tables():
    create_table()
    return {"message": "create tables"}


@router.get('/listById/{id}',response_model=ActomedicoOu)
def get_byId_actomedico(id:int,db:Session = Depends(get_db)):  
    return db.query(Actomedico).filter(Actomedico.id == id).first();


@router.post('/create')
def create_actomedico(ActomedicoIn:ActomedicoIn,db:Session = Depends(get_db)):

    row_item = Actomedico(**ActomedicoIn.dict(exclude={'antecedentes','diagnosticos','recetas','idcita'}))
    db.add(row_item)
    db.commit()
    db.refresh(row_item)

    if row_item:
        db.query(Cita).filter(Cita.id == ActomedicoIn.idcita).update(dict({"estado":"A"}))
        db.commit()
        create_many_items(db,Antencedente,ActomedicoIn.dict().pop('antecedentes'),'idactomedico',row_item.id)
        create_many_items(db,Diagnostico,ActomedicoIn.dict().pop('diagnosticos'),'idactomedico',row_item.id)
        return {"message":"success"}


@router.put('/update/{idactomedico}')
def update_actomedico(idactomedico:int,ActomedicoIn:ActomedicoIn,db:Session = Depends(get_db)):

    data = db.query(Actomedico).filter(Actomedico.id == idactomedico).update(dict(ActomedicoIn.dict(exclude={'antecedentes','diagnosticos','recetas','idcita'})))
    db.commit()
    
    if data:
        create_many_items(db,Antencedente,ActomedicoIn.dict().pop('antecedentes'),'idactomedico',idactomedico)
        create_many_items(db,Diagnostico,ActomedicoIn.dict().pop('diagnosticos'),'idactomedico',idactomedico)
        return {"message":f''' Se actualizado el Acto medico'''}



def delete_actomedico_detalle(idactomedico:int,model:Base,db:Session):
    db.query(model).filter(model.idactomedico == idactomedico).delete()
    db.commit()

def create_many_items(db:Session,model:Base,bodys:list,field:str,idactomedico:int):
    delete_actomedico_detalle(idactomedico,model,db)
    for body in bodys:
        body[field] = idactomedico
        data = model(**body)
        db.add(data)
        db.commit()
        db.refresh(data)




