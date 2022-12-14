from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import (tarifario, tarifarioGrupo, tarifarioSubTitulo,
                    tarifarioTitulo)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tarifario)
app.include_router(tarifarioTitulo)
app.include_router(tarifarioSubTitulo)
app.include_router(tarifarioGrupo)