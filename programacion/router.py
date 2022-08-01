from fastapi import Depends,APIRouter, HTTPException
from models import Programacion
from schemas import ProgramacionSchema,ProgramacionBase
from sqlalchemy.orm import Session
from db import get_db


router = APIRouter(prefix='/programacion',tags=['Programacion'])


@router.get('/listAll')
def list_programacion(db:Session = Depends(get_db)):
    return db.query(Programacion).all()

@router.get('/listById/{id}',response_model =ProgramacionSchema)
def get_programacion(id:int,db:Session = Depends(get_db)):

    data = db.query(Programacion).filter(Programacion.id==id).first()

    if not data:
        raise HTTPException(status_code=404, detail='No hay data')

    return data


@router.post('/create')
def create_programacion(programacion:ProgramacionBase,db:Session = Depends(get_db)):
    row_item = Programacion(**programacion.dict())
    db.add(row_item)
    db.commit()
    db.refresh(row_item)
    return row_item


@router.put('/update/{id}')
def update_programacion(id:int,programacionBase:ProgramacionBase,db:Session = Depends(get_db)):

    data = db.query(Programacion).filter(Programacion.id == id).first()

    if not data:
        raise HTTPException(status_code=404, detail='Programacion no existe')

    for key,value in programacionBase.dict(exclude_unset=True).items():
        setattr(data,key,value)
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message":f''' Se actualizado'''}


@router.delete('delete/{id}')
def delete_programacion(id:int,db:Session = Depends(get_db)):
    
    data = db.query(Programacion).filter(Programacion.id == id).first()

    if not data:
        raise HTTPException(status_code=404, detail='No existe programacion')

    db.delete(data)
    db.commit()
    return {"message":f''' Se eleimino la programacion con el id {id} ''' }