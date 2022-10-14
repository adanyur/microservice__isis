from typing import List

from db import get_db
from fastapi import APIRouter, Depends
from models import Admision, create_table
from schemas import AdmisionBase
from sqlalchemy import distinct
from sqlalchemy.orm import Session

router = APIRouter(prefix='/admision',tags=['Admision'])

@router.get('/createTables')
def creates_tables():
    create_table()
    return {"message": "create tables"}



@router.post('/create')
def create_admision(AdmisionBase:AdmisionBase,db:Session = Depends(get_db)):

    admision = db.query(Admision).filter(Admision.idcita == AdmisionBase.idcita).first()
    if admision:
        return {"message": "la cita ya tiene una admision generada"}


    row_item = Admision(**AdmisionBase.dict(exclude={'persona'}))
    db.add(row_item)
    db.commit()
    return {"message": "Se genero la admision"}