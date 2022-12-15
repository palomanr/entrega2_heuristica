#!/bin/bash
echo --------------------PRUEBA 1 Parte delantera del bus llena ------------------------------------
python3 CSPCargaBUS.py ./CSP-tests/alumnos1.txt
echo --------------------PRUEBA 2 Parte trasera del bus llena---------------------------------------
python3 CSPCargaBUS.py ./CSP-tests/alumnos2.txt
echo --------------------PRUEBA 3 Parte delantera y trasera del bus medio llena --------------------
python3 CSPCargaBUS.py ./CSP-tests/alumnos3.txt
echo --------------------PRUEBA 4 Solo alumnos de movilidad normal----------------------------------
python3 CSPCargaBUS.py ./CSP-tests/alumnos4.txt
echo --------------------PRUEBA 5 Solo alumnos conflictivos-----------------------------------------
python3 CSPCargaBUS.py ./CSP-tests/alumnos5.txt