"""Funcion principal donde ejecutar la segunda parte"""

import os

from alumno import Alumno
from estado import Estado
from grafo import Grafo


def leer_entrada(ruta: str) -> dict:
    """Funcion para leer el fichero de entrada"""
    with open(ruta) as fichero:
        contenido = fichero.read()
    return eval(contenido)


def dict_alumnos(dict_obj: dict) -> list:
    """Funcion para convertir el diccionario en una lista"""
    alumnos = []
    for clave, valor in dict_obj.items():
        alumnos.append(Alumno(clave, valor))
    return alumnos


if __name__ == '__main__':
    """Main para ejecutar la parte 2"""
    estado = Estado()
    estado.de_dict(leer_entrada(os.getcwd() + "/test"))
    grafo = Grafo(estado)
    print(grafo.a_estrella().a_dict())
