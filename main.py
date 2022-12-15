import os

from alumno import Alumno
from estado import Estado
from grafo import Grafo


def leer_entrada(ruta: str) -> dict:
    with open(ruta) as fichero:
        contenido = fichero.read()
    return eval(contenido)


def dict_a_alumnos(dict_obj: dict) -> list:
    alumnos = []
    for clave, valor in dict_obj.items():
        alumnos.append(Alumno(clave, valor))
    return alumnos


if __name__ == '__main__':
    estado = Estado()
    estado.de_dict(leer_entrada(os.getcwd() + "/test"))
    grafo = Grafo(estado)
    print(grafo.a_estrella().a_dict())
