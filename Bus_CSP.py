import constraint
import sys
import numpy as np

#Obtain path from argument in bash
test_path = str(sys.argv[1])

#Get students from .txt file
alumnos = open(test_path, 'r').read().splitlines()

#Global lists of each type of student
alumnos_ciclo1 = []
alumnos_ciclo2 = []
alumnos_conflictivos = []
alumnos_conflictivos_no_hermano = []
alumnos_no_conflictivos = []
alumnos_mov_reducida = []
alumnos_mov_reducida_ciclo1 = []
alumnos_mov_reducida_ciclo2 = []
alumnos_mov_normal = []
alumnos_hermanos = []
alumnos_hermanos_no_conflictivos = []


alumnos_ciclo1_no_hermanos_mov_normal = []
alumnos_ciclo1_no_hermanos_mov_reducida = []

alumnos_ciclo2_no_hermanos_mov_normal = []
alumnos_ciclo2_no_hermanos_mov_reducida = []

alumnos_ciclo1_hermanos_mismo_ciclo_mov_normal = []
alumnos_ciclo1_hermanos_mismo_ciclo_mov_reducida = []

alumnos_ciclo2_hermanos_mismo_ciclo_mov_normal = []
alumnos_ciclo2_hermanos_mismo_ciclo_mov_reducida = []

alumnos_hermanos_ciclo_distinto_mov_normal = []
alumnos_hermanos_ciclo_distinto_mov_reducida = []



#Generate bus
array_asientos_bus = np.array([
                        [1,2,3,4], [5,6,7,8], 
                        [9, 10, 11, 12], [13, 14, 15, 16],
                        [17, 18, 19, 20], [21, 22, 23, 24],
                        [25, 26, 27, 28], [29, 30, 31, 32]])


#Filter each domain from main bus
dom_ciclo1_no_hermanos_mov_normal = np.concatenate([array_asientos_bus[0], array_asientos_bus[1], array_asientos_bus[2], array_asientos_bus[3]]).tolist()
dom_ciclo1_no_hermanos_mov_reducida = np.concatenate([array_asientos_bus[0], array_asientos_bus[3]]).tolist()

dom_ciclo2_no_hermanos_mov_normal = np.concatenate([array_asientos_bus[4], array_asientos_bus[5], array_asientos_bus[6], array_asientos_bus[7]]).tolist()
dom_ciclo2_no_hermanos_mov_reducida = np.concatenate([array_asientos_bus[4]]).tolist()

dom_alumnos_ciclo1_hermanos_mismo_ciclo_mov_normal = np.concatenate([array_asientos_bus[0], array_asientos_bus[1], array_asientos_bus[2], array_asientos_bus[3]]).tolist()
dom_alumnos_ciclo1_hermanos_mismo_ciclo_mov_reducida = np.concatenate([array_asientos_bus[0], array_asientos_bus[3]]).tolist()

dom_alumnos_ciclo2_hermanos_mismo_ciclo_mov_normal = np.concatenate([array_asientos_bus[4], array_asientos_bus[5], array_asientos_bus[6], array_asientos_bus[7]]).tolist()
dom_alumnos_ciclo2_hermanos_mismo_ciclo_mov_reducida = np.concatenate([array_asientos_bus[4]]).tolist()

dom_alumnos_hermanos_ciclo_distinto_mov_normal = np.concatenate([array_asientos_bus[0], array_asientos_bus[1], array_asientos_bus[2], array_asientos_bus[3]]).tolist()
dom_alumnos_hermanos_ciclo_distinto_mov_reducida = np.concatenate([array_asientos_bus[0], array_asientos_bus[3]]).tolist()





#All filter functions that add each student to tehir corresponding list
def filter_confllictivo_no_hermano(alumno, datos_alumno):
    if datos_alumno[2] == 'C':
        if int(datos_alumno[4]) == 0:
            alumnos_conflictivos_no_hermano.append(alumno)

def filter_hermanos_no_conflictivos(alumno, datos_alumno):
    if int(datos_alumno[4]) > 0 :
        if datos_alumno[2] == 'X': 
            alumnos_hermanos_no_conflictivos.append(alumno)


def filter_ciclio(alumno, datos_alumno):
    if datos_alumno[1]  == '1':
        if datos_alumno[3] == 'R':
            alumnos_mov_reducida_ciclo1.append(alumno)

    if datos_alumno[1] == '2':
        if datos_alumno[3] == 'R':
            alumnos_mov_reducida_ciclo2.append(alumno)

def filter_mov_reducida_ciclio(alumno, datos_alumno):
    if datos_alumno[1]  == '1':
        alumnos_ciclo1.append(alumno)

    if datos_alumno[1] == '2':
        alumnos_ciclo2.append(alumno)

def filter_ciclo_no_hermanos_mov(alumno, datos_alumno):
    #Students cycle 1, no bothers and regular mobility
    if (datos_alumno[1]  == '1') and (int(datos_alumno[4]) == 0) and ((datos_alumno[3] == 'X')):
        alumnos_ciclo1_no_hermanos_mov_normal.append(alumno)

    #Students cycle 1, no bothers and reduced mobility
    if (datos_alumno[1] == '1') and (int(datos_alumno[4]) == 0) and ((datos_alumno[3] == 'R')):
        alumnos_ciclo1_no_hermanos_mov_reducida.append(alumno)

    #Students cycle 2, no bothers and regular mobility
    if (datos_alumno[1]  == '2') and (int(datos_alumno[4]) == 0) and ((datos_alumno[3] == 'X')):
            alumnos_ciclo2_no_hermanos_mov_normal.append(alumno)

    #Students cycle 2, no bothers and reduced mobility
    if (datos_alumno[1] == '2') and (int(datos_alumno[4]) == 0) and ((datos_alumno[3] == 'R')):
        alumnos_ciclo2_no_hermanos_mov_reducida.append(alumno)

def filter_ciclo_hermanos_mismo_ciclo_mov(alumno, datos_alumno):
    #Students brothers both in cycle 1, and 1 is regular mobility
    if (datos_alumno[1]  == '1') and ((int(datos_alumno[4])) > 0) and ((datos_alumno[3] == 'X')):
        #Check if brother is also same cycle
        brother_id = datos_alumno[4]
        for possible_borther in alumnos:
            datos_possible_borther = possible_borther.split(",")
            if (datos_possible_borther[0]  == brother_id):
                if (datos_possible_borther[1] == '1'):
                    alumnos_ciclo1_hermanos_mismo_ciclo_mov_normal.append(alumno)

    #Students brothers both in cycle 1, and 1 is regular reduced
    if (datos_alumno[1]  == '1') and ((int(datos_alumno[4])) > 0) and ((datos_alumno[3] == 'R')):
        #Check if brother is also same cycle
        brother_id = datos_alumno[4]
        for possible_borther in alumnos:
            datos_possible_borther = possible_borther.split(",")
            if (datos_possible_borther[0]  == brother_id):
                if (datos_possible_borther[1] == '1'):
                    alumnos_ciclo1_hermanos_mismo_ciclo_mov_reducida.append(alumno)

    if (datos_alumno[1]  == '2') and ((int(datos_alumno[4])) > 0) and ((datos_alumno[3] == 'X')):
        #Check if brother is also same cycle
        brother_id = datos_alumno[4]
        for possible_borther in alumnos:
            datos_possible_borther = possible_borther.split(",")
            if (datos_possible_borther[0]  == brother_id):
                if (datos_possible_borther[1] == '2'):
                    alumnos_ciclo2_hermanos_mismo_ciclo_mov_normal.append(alumno)

    #Students brothers both in cycle 1, and 1 is regular reduced
    if (datos_alumno[1]  == '2') and ((int(datos_alumno[4])) > 0) and ((datos_alumno[3] == 'R')):
        #Check if brother is also same cycle
        brother_id = datos_alumno[4]
        for possible_borther in alumnos:
            datos_possible_borther = possible_borther.split(",")
            if (datos_possible_borther[0]  == brother_id):
                if (datos_possible_borther[1] == '2'):
                    alumnos_ciclo2_hermanos_mismo_ciclo_mov_reducida.append(alumno)


def filter_hermanos_ciclo_distinto_mov(alumno, datos_alumno):
    #Students brothers both in cycle 1, and 1 is regular mobility
    if ((int(datos_alumno[4])) > 0) and ((datos_alumno[3] == 'X')):
        #Check if brother is in diffrent cycle
        brother_id = datos_alumno[4]
        for possible_borther in alumnos:
            datos_possible_borther = possible_borther.split(",")
            if (datos_possible_borther[0]  == brother_id):
                if (datos_possible_borther[1] != datos_alumno[1]):
                    alumnos_hermanos_ciclo_distinto_mov_normal.append(alumno)

    if ((int(datos_alumno[4])) > 0) and ((datos_alumno[3] == 'R')):
        #Check if brother is in diffrent cycle
        brother_id = datos_alumno[4]
        for possible_borther in alumnos:
            datos_possible_borther = possible_borther.split(",")
            if (datos_possible_borther[0]  == brother_id):
                if (datos_possible_borther[1] != datos_alumno[1]):
                    alumnos_hermanos_ciclo_distinto_mov_reducida.append(alumno)


def filter_confllictivo(alumno, datos_alumno):
    if datos_alumno[2] == 'C':
        alumnos_conflictivos.append(alumno)
    if datos_alumno[2] == 'X': 
        alumnos_no_conflictivos.append(alumno)

def filter_movilidad(alumno, datos_alumno):
    if datos_alumno[3] == 'R':
        alumnos_mov_reducida.append(alumno)
    if datos_alumno[3] == 'X': 
        alumnos_mov_normal.append(alumno)

def filter_hermanos(alumno, datos_alumno):
    if int(datos_alumno[4]) > 0 :
        alumnos_hermanos.append(alumno)


# Constrait functions
# -------------------------------------------------------------------------
def next_seat_clear_cicle1(alumno1, alumno2):
    if(alumno1 == 1 and alumno2 != 2):
        return True
    if(alumno1 == 2 and alumno2 != 1):
        return True
    if(alumno1 == 3 and alumno2 != 4):
        return True
    if(alumno1 == 4 and alumno2 != 3):
        return True
    if(alumno1 == 13 and alumno2 != 14):
        return True
    if(alumno1 == 14 and alumno2 != 13):
        return True
    if(alumno1 == 15 and alumno2 != 16):
        return True
    if(alumno1 == 16 and alumno2 != 15):
        return True

def next_seat_clear_cicle2(alumno1, alumno2):
    if(alumno1 == 17 and alumno2 != 18):
        return True
    if(alumno1 == 18 and alumno2 != 17):
        return True
    if(alumno1 == 19 and alumno2 != 20):
        return True
    if(alumno1 == 20 and alumno2 != 19):
        return True

def nobody_arround_conflictivo(alumno_conf, alumno):
    if((alumno_conf + 1 != alumno) and (alumno_conf + 3 != alumno) and (alumno_conf + 4 != alumno) and (alumno_conf + 5 != alumno)):
        if((alumno_conf - 1 != alumno) and (alumno_conf - 3 != alumno) and (alumno_conf - 4 != alumno) and (alumno_conf - 5 != alumno)):
            return True

def brothers_together_no_conflictivo(brother1, brother2):
   for asiento in array_asientos_bus:
        for i in range (3):
            """if brother1 == asiento[i]: 
                print(True, "The value of borther 1 is: ", brother1, "and the value of brother 2 is: ", brother2)
            if brother2 == asiento[1+1]:
                #print("brother 2 ok ")"""
            if((brother1 == asiento[i]) and (brother2 == asiento[i+1])):
                return True
            if((brother2 == asiento[i]) and (brother1 == asiento[i+1])):
                return True

            

#Creating a CSP problem
problem = constraint.Problem()


for alumno in alumnos:
    datos_alumno = alumno.split(",")
    filter_confllictivo_no_hermano(alumno, datos_alumno)
    filter_hermanos_no_conflictivos(alumno, datos_alumno)
    filter_hermanos(alumno, datos_alumno)
    filter_confllictivo(alumno, datos_alumno)
    filter_ciclio(alumno, datos_alumno)
    filter_ciclo_no_hermanos_mov(alumno, datos_alumno)
    filter_ciclo_hermanos_mismo_ciclo_mov(alumno, datos_alumno)
    filter_hermanos_ciclo_distinto_mov(alumno, datos_alumno)


# variables
# -----------------------------------------------------------------------

problem.addVariables(alumnos_ciclo1_no_hermanos_mov_normal, dom_ciclo1_no_hermanos_mov_normal)
problem.addVariables(alumnos_ciclo1_no_hermanos_mov_reducida, dom_ciclo1_no_hermanos_mov_reducida)

problem.addVariables(alumnos_ciclo2_no_hermanos_mov_normal, dom_ciclo2_no_hermanos_mov_normal)
problem.addVariables(alumnos_ciclo2_no_hermanos_mov_reducida, dom_ciclo2_no_hermanos_mov_reducida)

problem.addVariables(alumnos_ciclo1_hermanos_mismo_ciclo_mov_normal, dom_alumnos_ciclo1_hermanos_mismo_ciclo_mov_normal)
problem.addVariables(alumnos_ciclo1_hermanos_mismo_ciclo_mov_reducida, dom_alumnos_ciclo1_hermanos_mismo_ciclo_mov_reducida)

problem.addVariables(alumnos_ciclo2_hermanos_mismo_ciclo_mov_normal, dom_alumnos_ciclo2_hermanos_mismo_ciclo_mov_normal)
problem.addVariables(alumnos_ciclo2_hermanos_mismo_ciclo_mov_reducida, dom_alumnos_ciclo2_hermanos_mismo_ciclo_mov_reducida)

problem.addVariables(alumnos_hermanos_ciclo_distinto_mov_normal, dom_alumnos_hermanos_ciclo_distinto_mov_normal)
problem.addVariables(alumnos_hermanos_ciclo_distinto_mov_reducida, dom_alumnos_hermanos_ciclo_distinto_mov_reducida)

# Constraits
# -------------------------------------------------------------------------

problem.addConstraint(constraint.AllDifferentConstraint())

for alumno_mov_reducida_ciclo1 in alumnos_mov_reducida_ciclo1:
    for alumno in alumnos:
        problem.addConstraint(next_seat_clear_cicle1, (alumno_mov_reducida_ciclo1, alumno))

for alumno_mov_reducida_ciclo2 in alumnos_mov_reducida_ciclo2:
    for alumno in alumnos:
        problem.addConstraint(next_seat_clear_cicle2, (alumno_mov_reducida_ciclo2, alumno))

for alumno_confilctivo in alumnos_conflictivos_no_hermano:
    for alumno in alumnos:
        problem.addConstraint(nobody_arround_conflictivo, (alumno_confilctivo, alumno))
problem.addConstraint(brothers_together_no_conflictivo, (alumnos_hermanos_no_conflictivos[0] , alumnos_hermanos_no_conflictivos[1] ))
    
    



# Solution
# -------------------------------------------------------------------------
print(problem.getSolution())

#print(problem.getSolutions())

"""

print("Alumnos no hermanos: ")
print(alumnos_ciclo1_no_hermanos_mov_normal)
print(alumnos_ciclo1_no_hermanos_mov_reducida)
print(alumnos_ciclo2_no_hermanos_mov_normal)
print(alumnos_ciclo2_no_hermanos_mov_reducida)

print("Alumnos hermanos mismo Ciclo: ")
print(alumnos_ciclo1_hermanos_mismo_ciclo_mov_normal)
print(alumnos_ciclo1_hermanos_mismo_ciclo_mov_reducida)
print(alumnos_ciclo2_hermanos_mismo_ciclo_mov_normal)
print(alumnos_ciclo2_hermanos_mismo_ciclo_mov_reducida)

print("Alumnos hermanos Ciclo distintos: ")
print(alumnos_hermanos_ciclo_distinto_mov_reducida)
print(alumnos_hermanos_ciclo_distinto_mov_normal)


print(alumnos_mov_normal)
print(alumnos_mov_reducida)
print((list_dom_alumnos))
print(list_dom_mov_reducida)

"""

"""
print('Alumnos Ciclio 1: ', alumnos_ciclio1)
print('Alumnos Ciclio 2: ', alumnos_ciclio2)
print('Alumnos Conflictivos: ', alumnos_conflictivos)
print('Alumnos Mov Reducida: ', alumnos_mov_reducida)
print('Alumnos Con Hemanos:  ', alumnos_hermanos)"""