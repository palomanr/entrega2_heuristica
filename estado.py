"""FICHERO PARA DEFINIR LOS ESTADOS DEL A*"""
from alumno import Alumno


class Estado:
    def __init__(self, cola: list = None, no_asignado: list = None):
        if cola is None:
            self.cola = []
        else:
            self.cola = cola
        if no_asignado is None:
            self.no_asignado = []
        else:
            self.no_asignado = no_asignado
        self.g = self.calcular_g()
        self.h = self.calcular_h()
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __eq__(self, other):
        return self.f == other.f

    def __ne__(self, other):
        return self.f != other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f

    def calcular_g(self) -> int:
        costes = [1] * len(self.cola)
        alumnos_conflictivos = []
        for i in range(len(self.cola)):
            # Comprobando que no hay un estudiante de movilidad reducida al final de la cola
            if i == (len(self.cola) - 1) and self.cola[i].movilidad_reducida:
                return 999
            # Comprobando que no hay dos estudiantes de movilidad reducida seguidos
            try:
                if  self.cola[i].movilidad_reducida and self.self.cola[i+1].movilidad_reducida:
                    return 999
            except:
                pass
            # alumnos_conflictivos duplican el tiempo del alumno actual si está atras
            for j in alumnos_conflictivos:
                if self.cola[i].asiento > j.asiento:
                    costes[i] *= 2
            # incluimos en alumnos_conflictivos a los que lo sean
            if self.cola[i].conflictivo:
                alumnos_conflictivos.append(self.cola[i])
            # duplicar el costo de los alumnos que esten detras de uno conflictivo
            if i > 0 and self.cola[i - 1].conflictivo:
                costes[i] *= 2
            if i + 1 < len(self.cola) and self.cola[i + 1].conflictivo:
                costes[i] *= 2
            # si el actual es de movilidad reducida, triplicar el costo.
            if self.cola[i].movilidad_reducida:
                costes[i] *= 3
        # si se ayuda a un alumno con movilidad reducida, los costes se multiplican y se anula el correspondiente
        # al que ayuda.
        for i in range(len(self.cola)):
            if self.cola[i].movilidad_reducida and i + 1 < len(self.cola):
                costes[i] *= costes[i + 1]
                costes[i + 1] = 0
        # sumar todos los costes
        return sum(costes)

    def calcular_h(self) -> int:
        """calculamos las heuristicas"""
        conflictivos = 0
        movilidad_reducida = 0
        for e in self.cola:
            if e.conflictivo:
                conflictivos += 1
            if e.movilidad_reducida:
                movilidad_reducida += 1
        return len(self.cola) + conflictivos * 3 + movilidad_reducida * 2

    def es_meta(self) -> bool:
        return len(self.no_asignado) == 0

    def expandir(self) -> list:
        """FUNCION PARA EXPANDIR NODOS"""
        expandir = []
        for alumno in self.no_asignado:
            if not alumno.movilidad_reducida \
                    or (alumno.movilidad_reducida and len(self.cola) != 0 and not self.cola[-1].movilidad_reducida) \
                    or (alumno.movilidad_reducida and len(self.cola) == 0):
                cola = self.cola.copy()
                cola.append(alumno)
                sin_asignar = self.no_asignado.copy()
                sin_asignar.remove(alumno)
                expandir.append(Estado(cola, sin_asignar))
        expandir.sort()
        return expandir

    def de_dict(self, dict_obj: dict) -> None:
        for clave, valor in dict_obj.items():
            self.no_asignado.append(Alumno(clave, valor))

    def a_dict(self) -> dict:
        a_dict = {}
        for i in self.cola:
            a_dict[i.clave] = i.asiento
        return a_dict
