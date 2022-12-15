"""Funcion principal donde ejecutar la segunda parte"""

import os

from alumno import Alumno
from estado import Estado
from grafo import Grafo
import time
from fn_heu2 import Calcular_g2


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
    start = time.time()
    result = grafo.a_estrella().a_dict()
    print(grafo.a_estrella().a_dict())
    end = time.time()
    tiempo_total = end - start
    print("\nTiempo total: ", tiempo_total)
    # Calculando e imprimiendo coste total con otra función heurística
    print("\nCoste de cola inicial: ", Calcular_g2.calculate(leer_entrada(os.getcwd() + "/test")))
    print("\nCoste de cola optimizada: ", Calcular_g2.calculate(grafo.a_estrella().a_dict()))


