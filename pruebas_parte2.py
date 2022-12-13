"""CODIGO PRUEBA PROGRAMAR A* Y DEMÁS"""
#pagina útil
# https://programmerclick.com/article/7502407898

#recibe
entrada = {'3XX': 11, '1CX': 12, '6XX': 15, '5XX': 16,
           '8XR': 18, '4CR': 20, '2XX': 31, '7CX': 32}
ESTADO_INICIAL = []


# ESTADO_FINAL = [LLENA]

class Aestrella():
    def __init__(self, entrada_parte1) -> None:
        self.cola = Cola()

        # Nodos que esperan ser expandidos en orden creciente de f(n)
        self.abierta = [self.cola]

        # Nodos que esperan expandidos se detecta duplicados
        self.cerrada = []

        self.lista_alumnos = []

        self.entrada = entrada_parte1

    def generar_estadisticas(self):

        pass

    def parsear_entrada(self):
        self.lista_alumnos = []
        self.entrada = self.entrada.keys()
        print("Claves")
        for n in self.entrada:
            alumno = Alumnos(n[0], n[1], n[2])
            self.lista_alumnos.append(alumno)

    def mostrar_soluciones(self):
        pass

    def algoritmo_A(self):

        exito = False

        while True:
            if len(self.abierta) != 0 or exito == False:
                estado = self.abierta.pop()
                if estado not in self.cerrada:

                    # Si estado es estado final
                    if len(estado) == len(self.lista_alumnos):
                        exito = True
                    else:
                        self.cerrada.append(estado)

                        # Si abierta esta vacia -> Es la primera poscion de la cola, por lo qeu se podra añadir cualquier alumno
                        if len(self.abierta) == 0:
                            for alumno in self.lista_alumnos:
                                # Añadimos cada posible alumno a la lista abierta
                                self.abierta.append(Cola().al)
                        else:
                            if self.abierta[-1] == "R":
                                lista_actualizada_sin_mr = []
                                for alumno in self.lista_alumnos:
                                    if alumno.

                        for n in
                            if self.
                                self.abierta.append(self.cola.añadir_alumno())


class Alumnos():
    """DEFINIMOS LOS ALUMNOS"""

    def __init__(self, id, conflictivo, movilidad):
        self.id = id
        self.conflictivo = conflictivo
        self.movilidad = movilidad

        # F = G + H
        # G = el costo de moverse desde el punto de partida A al cuadrado especificado
        # H = El costo estimado de mudarse del cuadrado especificado al destino B. Heurística Aquí se usa el método Manhattan para estimar H
        self.G = 0
        self.H = 0

    def __str__(self):
        cadena = "Id del alumno: " + self.id + "\n" + "Es conflictivo el alumno?: " + self.conflictivo + "\n" + "El alumno tienen movilidad redicida?: " + self.movilidad + "\n"
        return cadena


class Cola():
    def __init__(self):
        self.cola = []
        self.tiempo = 0

    def añadir_alumno(self, alumno: object):
        if len(self.cola) == 0:
            self.cola.append(alumno)

        else:
            if self.cola[-1].conflictivo == "C":
                pass
            if self.cola[-1].movilidad == "R":
                pass
        if

    def sacar_alumno(self):
        self.cola.pop()

    def mostrar_cola(self):
        for n in range(len(self.cola)):
            print(self.cola[n])


cola = Cola([], 0)
alumno1 = Alumnos("8", "X", "R")
alumno2 = Alumnos("2", "C", "R")
cola.añadir_alumno(alumno1)
cola.añadir_alumno(alumno1)

cola.mostrar_cola()
