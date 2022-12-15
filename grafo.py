"""FUNCION PARA HACER EL A*"""
from estado import Estado


class Grafo:
    """CLASE CON EL GRAFO, TENEMOS UNA LISTA ABIERTA INICIAL Y LA CERRADA QUE AL PRINCIPIO NO HAY NADA"""
    def __init__(self, estado: Estado):
        self.abierta = [estado]
        self.cerrada = []
        self.exito = False

    def a_estrella(self) -> Estado:
        """FUNCION CON EL ALGORITMO A* VISTO EN CLASE DE TEORIA"""
        while len(self.abierta) > 0 and not self.exito:
            nodo = self.abierta.pop(0)
            self.cerrada.append(nodo)
            if nodo.es_meta():
                self.exito = True
                break
            self.abierta += nodo.expandir()
            self.abierta.sort()
        if not self.exito:
            raise Exception("No es posible conseguir una solucion que satisfaga las restricciones.")
        return self.cerrada[-1]



