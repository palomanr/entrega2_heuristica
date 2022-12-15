import datetime
import sys


class Alumno:
    def __init__(self, clave, asiento):
        self.id = int(clave[0:-2])
        self.conflictivo = clave[-2] == 'C'
        self.movilidad_reducida = clave[-1] == 'R'
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
        """ Propiedad que retorna un str con la clave del diccionario del alumno. """
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
    def __init__(self, cola: list = None, sin_asignar: list = None, profundidad: int = 0, heuristica: int = 0):
        if cola is None:
            self.cola = []
        else:
            self.cola = cola
        if sin_asignar is None:
            self.sin_asignar = []
        else:
            self.sin_asignar = sin_asignar
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
        """ Metodo que devuelve el peso del estado. """
        costes = [1] * len(self.cola)
        conflictivos = []
        for i in range(len(self.cola)):
            # Recorrer los conflictivos que han entrado. Duplican el tiempo del alumno actual si este se sienta atras.
            for j in conflictivos:
                if self.cola[i].asiento > j.asiento:
                    costes[i] *= 2
            # Si es conflictivo, anadirlo a los conflictivos.
            if self.cola[i].conflictivo:
                conflictivos.append(self.cola[i])
            # Si el anterior es conflictivo, duplicar el coste.
            if i > 0 and self.cola[i - 1].conflictivo:
                costes[i] *= 2
            # Si el siguiente es conflictivo, duplicar el coste.
            if i + 1 < len(self.cola) and self.cola[i + 1].conflictivo:
                costes[i] *= 2
            # Si el actual es de movilidad reducida, triplicar el coste.
            if self.cola[i].movilidad_reducida:
                costes[i] *= 3
        # Si se ayuda a un alumno con movilidad reducida, los costes se multiplican y se anula el del acompanante.
        for i in range(len(self.cola)):
            if self.cola[i].movilidad_reducida and i + 1 < len(self.cola):
                costes[i] *= costes[i + 1]
                costes[i + 1] = 0
        # Se suman todos los costes
        return sum(costes)

    def calcular_h(self, heuristica: int) -> int:
        """ Metodo que devuelve el valor heuristico del estado. """
        if heuristica == 1:
            return self.calcular_h_1()
        if heuristica == 2:
            return self.calcular_h_2()
        return 0

    def calcular_h_1(self) -> int:
        """ Metodo que devuelve el valor heuristico del estado usando la heuristica 1. """
        conflictivos = 0
        movilidad_reducida = 0
        for e in self.cola:
            if e.conflictivo:
                conflictivos += 1
            if e.movilidad_reducida:
                movilidad_reducida += 1
        return len(self.cola) + conflictivos * 3 + movilidad_reducida * 2

    def calcular_h_2(self) -> int:
        """ Metodo que devuelve el valor heuristico del estado usando la heuristica 2. """
        ...

    def es_meta(self) -> bool:
        """ Metodo que indica si el estado es un estado meta. """
        return len(self.sin_asignar) == 0

    def expandir(self, heuristica: int) -> list:
        """ Metodo que devuelve una lista con los estados obtenidos tras expandir el actual. """
        expandir = []
        for alumno in self.sin_asignar:
            if self.futuro_valido(alumno):
                cola = self.cola.copy()
                cola.append(alumno)
                sin_asignar = self.sin_asignar.copy()
                sin_asignar.remove(alumno)
                expandir.append(Estado(cola, sin_asignar, self.profundidad + 1, heuristica))
        expandir.sort()
        return expandir

    def de_dict(self, dict_entrada: dict) -> None:
        """ Metodo que anade a la cola los alumnos de un diccionario. """
        for clave, valor in dict_entrada.items():
            self.sin_asignar.append(Alumno(clave, valor))

    def a_dict(self) -> dict:
        """ Metodo que devuelve la cola de un estado como un diccionario. """
        a_dict = {}
        for i in self.cola:
            a_dict[i.clave] = i.asiento
        return a_dict

    def futuro_valido(self, alumno: Alumno) -> bool:
        """ Metodo que indica si un futuro estado sera valido. """
        """ Existen ayudantes para todos los alumnos con movilidad reducida y 
        el actual no tiene movilidad reducida o es el primero en la cola o el anterior no tiene movilidad reducida. """
        return self.quedan_ayudantes(alumno) \
            and (not alumno.movilidad_reducida or len(self.cola) == 0 or not self.cola[-1].movilidad_reducida)

    def quedan_ayudantes(self, alumno: Alumno) -> bool:
        """ Metodo que indica si en un futuro estado habra ayudantes suficientes para los alumnos con movilidad
        reducida. """
        movilidad_reducida = 0
        for i in self.sin_asignar:
            if i.movilidad_reducida:
                movilidad_reducida += 1
        movilidad_normal = len(self.sin_asignar) - movilidad_reducida
        if not alumno.movilidad_reducida:
            movilidad_normal -= 1
        return movilidad_reducida <= movilidad_normal


class AEstrella:
    def __init__(self, dict_alumnos: dict, heuristica: int):
        estado = Estado(heuristica=heuristica)
        estado.de_dict(dict_alumnos)
        self.abierta = [estado]
        self.expandidos = 0
        self.heuristica = heuristica
        self.meta = Estado()
        self.tiempo = 0

    def ejecutar(self) -> None:
        """ Metodo que ejecuta el algoritmo A*. """
        principio = datetime.datetime.now()
        while len(self.abierta) > 0:
            nodo = self.abierta.pop(0)
            if nodo.es_meta():
                self.meta = nodo
                diferencia_tiempo = datetime.datetime.now() - principio
                self.tiempo = diferencia_tiempo.total_seconds()
                return
            self.abierta += nodo.expandir(self.heuristica)
            self.expandidos += 1
            self.abierta.sort()
        raise Exception('Es imposible obtener una solucion que satisfaga las restricciones.')

    @property
    def stat(self) -> str:
        """ Propiedad que devuelve el contenido del fichero stat. """
        return 'Tiempo total: ' + str(self.tiempo) \
            + '\nCoste total: ' + str(self.meta.g) \
            + '\nLongitud del plan: ' + str(self.meta.profundidad) \
            + '\nNodos expandidos: ' + str(self.expandidos)


def leer_entrada(ruta: str) -> dict:
    """ Funcion que lee un fichero de entrada y lo devuelve como un diccionario. """
    with open(ruta) as fichero:
        contenido = fichero.read()
    entrada = eval(contenido)
    if not isinstance(entrada, dict):
        raise Exception('Fichero de entrada invalido.')
    return entrada


def escribir_salida(ruta: str, aestrella_ejecutado: AEstrella) -> None:
    """ Funcion que escribe dos ficheros de salida con los datos de la ejecucion. """
    escribir_salida_output(ruta, aestrella_ejecutado)
    escribir_salida_stat(ruta, aestrella_ejecutado)


def escribir_salida_output(ruta: str, aestrella_ejecutado: AEstrella) -> None:
    """ Funcion que escribe el fichero de salida .output con las configuraciones de la cola al inicio y al final. """
    output = "INICIAL:\t"
    with open(ruta) as fichero:
        output += fichero.read()
    output += "\nFINAL:\t" + str(aestrella_ejecutado.meta.a_dict())
    ruta_salida = ruta[:-5] + '-' + str(aestrella_ejecutado.heuristica) + '.output'
    with open(ruta_salida, 'w') as fichero:
        fichero.write(output)


def escribir_salida_stat(ruta: str, aestrella_ejecutado: AEstrella) -> None:
    """ Funcion que escribe el fichero de salida .stat con la informacion del proceso de busqueda. """
    ruta_salida = ruta[:-5] + '-' + str(aestrella_ejecutado.heuristica) + '.stat'
    with open(ruta_salida, 'w') as fichero:
        fichero.write(aestrella_ejecutado.stat)


if __name__ == '__main__':
    # Crear el Objeto con el diccionario del fichero de entrada y la heuristica deseada
    aestrella = AEstrella(leer_entrada(sys.argv[1]), int(sys.argv[2]))
    # Ejecutar el algoritmo A*
    aestrella.ejecutar()
    # Escribir los ficheros de salida
    escribir_salida(sys.argv[1], aestrella)
    print(aestrella.meta.a_dict())

