"""Fichero con la clase alumno y sus caracteristicas"""

class Alumno:
    """Un alumno puede ser conflictivo, de movilidad reducida o ninguna de las anteriores"""
    def __init__(self, clave, valor):
        self.id = int(clave[0:-2])
        self.conflictivo = clave[-2] == "C"
        self.movilidad_reducida = clave[-1] == "R"
        self.asiento = valor

    @property
    def clave(self):
        clave = str(self.id)
        if self.conflictivo:
            clave += "C"
        else:
            clave += "X"
        if self.movilidad_reducida:
            clave += "R"
        else:
            clave += "X"
        return clave
