from typing import List

from db import get_db
from fastapi import APIRouter, Depends
from models import (Tarifario, TarifarioGrupo, TarifarioSubtitulo,
                    TarifarioTitulo, create_table)
from sqlalchemy import distinct
from sqlalchemy.orm import Session

tarifario = APIRouter(prefix='/tarifario',tags=['Tarifario'])

@tarifario.get('/createTables')
async def creates_tables():
    create_table()
    return {"message": "create tables"}


@tarifario.get('/listados')
async def listado_tarifarios():
    return;

@tarifario.get('/create')
async def create_tarifario():
    return;

@tarifario.get('/update')
async def update_tarifario():
    return;


@tarifario.get('/delete')
async def delete_tarifarios():
    return;


tarifarioTitulo = APIRouter(prefix='/tarifariotitulo',tags=['Tarifario Titulo'])


@tarifarioTitulo.get('/listado')
async def listado_tarifarios(db:Session = Depends(get_db)):
    return db.query(TarifarioTitulo).all()


tarifarioSubTitulo = APIRouter(prefix='/tarifariosubtitulo',tags=['Tarifario Sub Titulo'])


@tarifarioSubTitulo.get('/listado')
async def listado_tarifarios():
    return;


tarifarioGrupo = APIRouter(prefix='/tarifariogrupo',tags=['Tarifario Grupo'])


@tarifarioGrupo.get('/listado')
async def listado_tarifarios(db:Session = Depends(get_db)):
    return db.query(TarifarioGrupo).all()