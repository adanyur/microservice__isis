from fastapi import Depends,APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import distinct
from models import create_table
#from schemas import ProgramacionSchema,ProgramacionBase,ProgramacionEspecialidadesEsquema,ProgramacionParameters,UpdateProgramacion
#from typing import List
#from sqlalchemy.orm import Session

from db import get_db


router = APIRouter(prefix='/consumo',tags=['Consumo'])


@router.get('/createTables')
def creates_tables():
    create_table()
    return {"message": "create tables"}