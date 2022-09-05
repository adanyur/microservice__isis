from fastapi import Depends,APIRouter, HTTPException
from sqlalchemy import distinct
from models import create_table,Admision
from typing import List
from sqlalchemy.orm import Session
from schemas import AdmisionBase
from db import get_db


router = APIRouter(prefix='/admision',tags=['Admision'])

@router.get('/createTables')
def creates_tables():
    create_table()
    return {"message": "create tables"}



@router.post('/create')
def create_admision(AdmisionBase:AdmisionBase,db:Session = Depends(get_db)):
    row_item = Admision(**AdmisionBase.dict(exclude={'persona'}))
    db.add(row_item)
    db.commit()
    # db.refresh(row_item)
    # return row_item
    return {"message": "successfully"}