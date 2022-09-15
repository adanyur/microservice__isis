from datetime import date, time
from base import ProgramacionIn


def calcularCupo(programacion:ProgramacionIn)->int:

    intervaloMedico = programacion.medico.intervalo.minute
    hora  = programacion.turno.horas.hour
    minute  = programacion.turno.horas.minute
    
    return int( ((hora * 60) + minute) / intervaloMedico)