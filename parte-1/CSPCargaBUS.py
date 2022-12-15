import constraint
import sys
import numpy as np

#First we obtain path from argument in bash
try:
    test_path = str(sys.argv[1])
except:
    print("El path indicado es inválido")

try:
    alumnos = open(test_path, 'r').read().splitlines()

except:
    print("Archivo corrompido o defectuoso")


#Global lists of each type of student (Self Explained)
#Lists for restricctions
alumnos_conflictivos = []
alumnos_conflictivos_no_hermano = []
alumnos_mov_reducida_ciclo1_no_hermano_ciclo_distinto = []
alumnos_mov_reducida_ciclo2_no_hermano_ciclo_distinto = []
alumnos_confllictivos_o_mov_reducida = []
alumnos_hermanos_mov_normal = []
alumnos_mov_reducida_hermano_ciclo_distinto = []

#Lists for domains
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

#Generate bus as an array
array_asientos_bus = np.array([
                        [1,2,3,4], [5,6,7,8], 
                        [9, 10, 11, 12], [13, 14, 15, 16],
                        [17, 18, 19, 20], [21, 22, 23, 24],
                        [25, 26, 27, 28], [29, 30, 31, 32]])


#Filter each domain from main bus arrangment
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





#All filter functions that add each student to their corresponding list for domain and restricctions
def filter_confllictivos_no_hermano(alumno, datos_alumno):
    #Students conflict with no brother
    if datos_alumno[2] == 'C':
        if int(datos_alumno[4]) == 0:
            alumnos_conflictivos_no_hermano.append(alumno)

def filter_hermanos_mov_normal(alumno, datos_alumno):
    #Students btother with regular mobility
    if datos_alumno[3] == 'X':
        brother_id = datos_alumno[4]
        for possible_borther in alumnos:
            datos_possible_borther = possible_borther.split(",")
            if (datos_possible_borther[0]  == brother_id):
                if (datos_possible_borther[3] == datos_alumno[3]):
                    alumnos_hermanos_mov_normal.append(alumno)

def filter_confllictivos_o_mov_reducida(alumno, datos_alumno):
    #conflict or reduced movility students
    if (datos_alumno[2] == 'C') or (datos_alumno[3] == 'R'):
            alumnos_confllictivos_o_mov_reducida.append(alumno)

def filter_ciclio(alumno, datos_alumno):
    #Students cycle filter
    if datos_alumno[1]  == '1':
        if datos_alumno[3] == 'R':
            if (int(datos_alumno[4]) == 0):
                alumnos_mov_reducida_ciclo1_no_hermano_ciclo_distinto.append(alumno)
            if (int(datos_alumno[4]) > 0):   
                brother_id = datos_alumno[4]
                for possible_borther in alumnos:
                    datos_possible_borther = possible_borther.split(",")
                    if (datos_possible_borther[0] == brother_id):
                        if (datos_possible_borther[1] == datos_alumno[1]):
                            alumnos_mov_reducida_ciclo1_no_hermano_ciclo_distinto.append(alumno)
                        else:
                            alumnos_mov_reducida_hermano_ciclo_distinto.append(alumno)

    if datos_alumno[1]  == '2':
        if datos_alumno[3] == 'R':
            if (int(datos_alumno[4]) == 0):
                alumnos_mov_reducida_ciclo2_no_hermano_ciclo_distinto.append(alumno)
            if (int(datos_alumno[4]) > 0):   
                brother_id = datos_alumno[4]
                for possible_borther in alumnos:
                    datos_possible_borther = possible_borther.split(",")
                    if (datos_possible_borther[0] == brother_id):
                        if (datos_possible_borther[1] == datos_alumno[1]):
                            alumnos_mov_reducida_ciclo2_no_hermano_ciclo_distinto.append(alumno)
                        else:
                            alumnos_mov_reducida_hermano_ciclo_distinto.append(alumno)

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


# Constrait functions
# -------------------------------------------------------------------------
def next_seat_clear_cicle1(alumno1, alumno2):
    if(alumno1 == 1 and alumno2 != 2) or (alumno1 == 2 and alumno2 != 1):
        return True
    if(alumno1 == 3 and alumno2 != 4) or (alumno1 == 4 and alumno2 != 3):
        return True
    if(alumno1 == 13 and alumno2 != 14) or (alumno1 == 14 and alumno2 != 13):
        return True
    if(alumno1 == 15 and alumno2 != 16) or (alumno1 == 16 and alumno2 != 15):
        return True

def next_seat_clear_cicle2(alumno1, alumno2):
    if(alumno1 == 17 and alumno2 != 18) or (alumno1 == 18 and alumno2 != 17):
        return True
    if(alumno1 == 19 and alumno2 != 20) or (alumno1 == 20 and alumno2 != 19):
        return True

def nobody_arround_conflictivo(alumno_conf, alumno):
    
    if((alumno_conf + 1 != alumno) and (alumno_conf + 3 != alumno) and (alumno_conf + 4 != alumno) and (alumno_conf + 5 != alumno)):
        if((alumno_conf - 1 != alumno) and (alumno_conf - 3 != alumno) and (alumno_conf - 4 != alumno) and (alumno_conf - 5 != alumno)):
            return True

def brothers_together(brother1, brother2):
    for asiento in array_asientos_bus:
        i = 0
        while i < 3:
            if((brother1 == asiento[i]) and (brother2 == asiento[i+1])):
                return True
            if((brother2 == asiento[i]) and (brother1 == asiento[i+1])):
                return True
            i = i+2

def brothers_together_big_brother_corridor(brother1, brother2):
    for asiento in array_asientos_bus:
        i = 0
        while i < 3:
            if i == 0:
                if((brother1 == asiento[i+1]) and (brother2 == asiento[i])):
                    return True
            if i == 2:
                if((brother1 == asiento[i]) and (brother2 == asiento[i+1])):
                    return True
            i = i+2

def fix_dict(solution):
    correct_keys = []
    value_keys = []
    for key , value in solution.items():
        datos_key = key.split(",")
        datos_key.pop(1)
        datos_key.pop(3)
        str_datos_key = ''.join(datos_key)
        correct_keys.append(str_datos_key)
        value_keys.append(value)

    correct_dict = dict(zip(correct_keys, value_keys))

    solution_dict = dict(sorted(correct_dict.items(), key = lambda x:x[1]))
    print("Solucion: ", solution_dict)
    return solution_dict     

def create_outputfile(test_path, solutions, solution_dict1, solution_dict2):
    with open(test_path + ".output", 'w') as f:
        f.write(" #Número de soluciones: {0} \n".format (len (solutions)))
        f.write("La primera solucion es: \n")
        f.write(str(solution_dict1))
        f.write("\nOtra solucion es: \n")
        f.write(str(solution_dict2))        

#Here we start the real code and main loop            
#Creating a CSP problem
problem = constraint.Problem()

#We filter each student
try:
    for alumno in alumnos:
        datos_alumno = alumno.split(",")
        filter_confllictivos_no_hermano(alumno, datos_alumno)
        filter_confllictivos_o_mov_reducida(alumno, datos_alumno)
        filter_hermanos_mov_normal(alumno, datos_alumno)
        filter_confllictivo(alumno, datos_alumno)
        filter_ciclio(alumno, datos_alumno)
        filter_ciclo_no_hermanos_mov(alumno, datos_alumno)
        filter_ciclo_hermanos_mismo_ciclo_mov(alumno, datos_alumno)
        filter_hermanos_ciclo_distinto_mov(alumno, datos_alumno)


    # Variables with each domain
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
    for alumno_mov_reducida_ciclo1 in alumnos_mov_reducida_ciclo1_no_hermano_ciclo_distinto:
        for alumno in alumnos:
            problem.addConstraint(next_seat_clear_cicle1, (alumno_mov_reducida_ciclo1, alumno))

    for alumno_mov_reducida_ciclo2 in alumnos_mov_reducida_ciclo2_no_hermano_ciclo_distinto:
        for alumno in alumnos:
            problem.addConstraint(next_seat_clear_cicle2, (alumno_mov_reducida_ciclo2, alumno))

    for alumno_mov_reducida_ciclo1 in alumnos_mov_reducida_hermano_ciclo_distinto:
        for alumno in alumnos:
            problem.addConstraint(next_seat_clear_cicle1, (alumno_mov_reducida_ciclo1, alumno))

    for alumno_confilctivo in alumnos_conflictivos:
        for alumno_confilctivo_o_mov_reducida in alumnos_confllictivos_o_mov_reducida:
            datos_alumno_confilctivo = alumno_confilctivo.split(",")
            datos_alumno_confilctivo_o_mov_reducida = alumno_confilctivo_o_mov_reducida.split(",")
            if datos_alumno_confilctivo[4] != datos_alumno_confilctivo_o_mov_reducida[0]:
                problem.addConstraint(nobody_arround_conflictivo, (alumno_confilctivo, alumno_confilctivo_o_mov_reducida))

    for hermano1 in alumnos_hermanos_mov_normal:
        for hermano2 in alumnos_hermanos_mov_normal:
            datos_hermano1 = hermano1.split(",")
            datos_hermano2 = hermano2.split(",")
            if datos_hermano1[0] == datos_hermano2[4]:
                if datos_hermano1[1] == datos_hermano2[1]:
                    problem.addConstraint(brothers_together, (hermano1, hermano2))
                if int(datos_hermano1[1]) > int(datos_hermano2[1]):
                    problem.addConstraint(brothers_together_big_brother_corridor, (hermano1, hermano2))
                if int(datos_hermano2[1]) > int(datos_hermano1[1]):
                    problem.addConstraint(brothers_together_big_brother_corridor, (hermano2, hermano1))


    # Solution
    # -------------------------------------------------------------------------
    solution1 = problem.getSolution()
    solutions = problem.getSolutions()
    solution2 = solutions[5]

    solution_dict1 = fix_dict(solution1)
    solution_dict2 = fix_dict(solution2)

    create_outputfile(test_path, solutions, solution_dict1, solution_dict2)

except:
    print("Formato invalido")