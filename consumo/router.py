from db import get_db
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from models import create_table
from sqlalchemy import distinct

#from schemas import ProgramacionSchema,ProgramacionBase,ProgramacionEspecialidadesEsquema,ProgramacionParameters,UpdateProgramacion
#from typing import List
#from sqlalchemy.orm import Session



router = APIRouter(prefix='/consumo',tags=['Consumo'])


@router.get('/createTables')
def creates_tables():
    create_table()
    return {"message": "create tables"}