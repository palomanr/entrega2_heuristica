"""PARTE 2 CODIGO"""
import datetime
import sys


class Alumno:
    """CLASE CON LA QUE DEFINIMOS A LOS ALUMNOS, SUS ID Y CARACTERISTICAS"""
    def __init__(self, id, asiento):
        self.id = int(id[0:-2])
        self.conflictivo = id[-2] == 'C'
        self.movilidad_reducida = id[-1] == 'R'
        self.asiento = asiento

    def __eq__(self, other):
        return self.id == other.id \
            and self.conflictivo == other.conflictivo \
            and self.movilidad_reducida == other.movilidad_reducida \
            and self.asiento == other.asiento

    def __ne__(self, other):
        return self.id != other.id \
            or self.conflictivo != other.conflictivo \
            or self.movilidad_reducida != other.movilidad_reducida \
            or self.asiento != other.asiento

    @property
    def clave(self):
        """ devuelve la id del diccionario del alumno. """
        clave = str(self.id)
        if self.conflictivo:
            clave += 'C'
        else:
            clave += 'X'
        if self.movilidad_reducida:
            clave += 'R'
        else:
            clave += 'X'
        return clave


class Estado:
    """CON ESTA CLASE DEFINIMOS LOS ESTADOS"""
    def __init__(self, cola: list = None, por_asignar: list = None, profundidad: int = 0, heuristica: int = 0):
        if cola is None:
            self.cola = []
        else:
            self.cola = cola
        if por_asignar is None:
            self.por_asignar = []
        else:
            self.por_asignar = por_asignar
        self.profundidad = profundidad
        self.g = self.calcular_g()
        self.h = self.calcular_h(heuristica)
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
        """ PARA CONSEGUIR EL COSTE DE MOVER DE UN ESTADO A OTRO
        los alumnols conflictivos duplican el tiempo del alumno actual si se sienta atras.
        conflictivo, anadirlo a los alumnos_conflictivos.
        anterior es conflictivo duplica el coste.
        siguiente es conflictivo, duplica el coste.
        si el actual es de movilidad reducida, triplicar el coste.
        ayuda a un alumno con movilidad reducida, los cost_list se multiplican y se anula el que tiene el ayudante."""
        cost_list = [1] * len(self.cola)
        alumnos_conflictivos = []
        for i in range(len(self.cola)):
            for j in alumnos_conflictivos:
                if self.cola[i].asiento > j.asiento:
                    cost_list[i] *= 2
            if self.cola[i].conflictivo:
                alumnos_conflictivos.append(self.cola[i])
            if i > 0 and self.cola[i - 1].conflictivo:
                cost_list[i] *= 2
            if i + 1 < len(self.cola) and self.cola[i + 1].conflictivo:
                cost_list[i] *= 2
            if self.cola[i].movilidad_reducida:
                cost_list[i] *= 3
        for i in range(len(self.cola)):
            if self.cola[i].movilidad_reducida and i + 1 < len(self.cola):
                cost_list[i] *= cost_list[i + 1]
                cost_list[i + 1] = 0
        total_cost = 0
        for current in cost_list:
            total_cost += current
        # Se suman todos los cost_list
        return total_cost

    def calcular_h(self, heuristica: int) -> int:
        """  devuelve el valor heuristico del estado. """
        if heuristica == 1:
            return self.calcular_h_1()
        if heuristica == 2:
            return self.calcular_h_2()
        if heuristica == 3:
            return self.calcular_h_3()
        if heuristica == 4:
            return self.calcular_h_4()
        return 0

    def calcular_h_1(self) -> int:
        """  usando la heuristica 1. """
        conflictivos = 0
        movilidad_reducida = 0
        for i in self.cola:
            if i.conflictivo:
                conflictivos += 1
            if i.movilidad_reducida:
                movilidad_reducida += 1
        return len(self.cola) + conflictivos * 3 + movilidad_reducida * 2

    def calcular_h_2(self) -> int:
        """ usando la heuristica 2. """
        conflictivos = 0
        movilidad_reducida = 0
        for i in self.cola:
            if i.conflictivo:
                conflictivos += 1
            if i.movilidad_reducida:
                movilidad_reducida += 1
        return len(self.cola) + conflictivos * 3 + movilidad_reducida

    def calcular_h_3(self) -> int:
        """  usando la heuristica 3. """
        conflictivos = 0
        movilidad_reducida = 0
        for i in self.cola:
            if i.conflictivo:
                conflictivos += 1
            if i.movilidad_reducida:
                movilidad_reducida += 1
        return len(self.cola) + conflictivos + movilidad_reducida * 2

    def calcular_h_4(self) -> int:
        """  usando la heuristica 4. """
        conflictivos = 0
        movilidad_reducida = 0
        for i in self.cola:
            if i.conflictivo:
                conflictivos += 1
            if i.movilidad_reducida:
                movilidad_reducida += 1
        return len(self.cola) + conflictivos + movilidad_reducida

    def llegamos_goal(self) -> bool:
        return len(self.por_asignar) == 0

    def expandir(self, heuristica: int) -> list:
        """  lista con los estados despues de expandir """
        expandir = []
        for alumno in self.por_asignar:
            if self.estado_siguiente_adecuado(alumno):
                cola = self.cola.copy()
                cola.append(alumno)
                sin_asignar = self.por_asignar.copy()
                sin_asignar.remove(alumno)
                expandir.append(Estado(cola, sin_asignar, self.profundidad + 1, heuristica))
        expandir.sort()
        return expandir

    def de_dict(self, dict_entrada: dict) -> None:
        """ incluimos a la cola los alumnos de un diccionario. """
        for id, caracteristica in dict_entrada.items():
            self.por_asignar.append(Alumno(id, caracteristica))

    def a_dict(self) -> dict:
        """ cola de un estado como un diccionario """
        a_dict = {}
        for i in self.cola:
            a_dict[i.clave] = i.asiento
        return a_dict

    def estado_siguiente_adecuado(self, alumno: Alumno) -> bool:
        """ hay ayudantes para los alumnos """
        return self.alumnos_que_ayudan(alumno) \
            and (not alumno.movilidad_reducida or len(self.cola) == 0 or not self.cola[-1].movilidad_reducida)

    def alumnos_que_ayudan(self, alumno: Alumno) -> bool:
        """ ver si en el siguiente estado habrán suficientes alumnos para ayudar a los de mov. reducida"""
        movilidad_reducida = 0
        for i in self.por_asignar:
            if i.movilidad_reducida:
                movilidad_reducida += 1
        alumno_sin_reducida = len(self.por_asignar) - movilidad_reducida
        if not alumno.movilidad_reducida:
            alumno_sin_reducida -= 1
        return movilidad_reducida <= alumno_sin_reducida


class AEstrella:
    def __init__(self, dict_alumnos: dict, heuristica: int):
        estado = Estado(heuristica=heuristica)
        estado.de_dict(dict_alumnos)
        self.heuristica = heuristica
        self.meta = Estado()
        self.tiempo = 0
        self.expandidos = 0
        self.abierta = [estado]


    def ejecutar(self) -> None:
        """ algoritmo A*. """
        inicio = datetime.datetime.now()
        while len(self.abierta) > 0:
            nodo = self.abierta.pop(0)
            if nodo.llegamos_goal():
                self.meta = nodo
                diferencia_tiempo = datetime.datetime.now() - inicio
                self.tiempo = diferencia_tiempo.total_seconds()
                return
            self.abierta += nodo.expandir(self.heuristica)
            self.expandidos += 1
            self.abierta.sort()
        raise Exception('imposible conseguir una solucion que satisfaga las restricciones.')

    @property
    def stat(self) -> str:
        """  devuelve el contenido del fichero de estadisticas """
        return 'Tiempo total: ' + str(self.tiempo) \
            + '\nCoste total: ' + str(self.meta.g) \
            + '\nLongitud del plan: ' + str(self.meta.profundidad) \
            + '\nNodos expandidos: ' + str(self.expandidos)


def leer_entrada(ruta: str) -> dict:
    """ fichero entrada devuelto como diccionario """
    with open(ruta) as fichero:
        fichero_interior = fichero.read()
    entrada = eval(fichero_interior)
    if not isinstance(entrada, dict):
        raise Exception('Fichero de entrada no es correcto.')
    return entrada

def escribir_salida(ruta: str, aestrella_ejecutado: AEstrella) -> None:
    """  fichero de salida  configuraciones de la cola inicio y  final. """
    output = "INICIAL:\t"
    with open(ruta) as fichero:
        output += fichero.read()
    output += "\nFINAL:\t" + str(aestrella_ejecutado.meta.a_dict())
    ruta_salida = ruta[:-5] + '-' + str(aestrella_ejecutado.heuristica) + '.output'
    with open(ruta_salida, 'w') as fichero:
        fichero.write(output)
    """  fichero de salida estadisticas """
    ruta_salida = ruta[:-5] + '-' + str(aestrella_ejecutado.heuristica) + '.stat'
    with open(ruta_salida, 'w') as fichero:
        fichero.write(aestrella_ejecutado.stat)


if __name__ == '__main__':
    aestrella = AEstrella(leer_entrada(sys.argv[1]), int(sys.argv[2]))
    aestrella.ejecutar()
    escribir_salida(sys.argv[1], aestrella)
    print(aestrella.meta.a_dict())

