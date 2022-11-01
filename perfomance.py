"""
 * Fecha: 31-Octubre-2022
 * Autor: Yeison Lizcano
 * Materia: Parallel and Distributed Computing
 * Tema: Medida de rendimiento cython/python: Problema Planeta en Orbita
"""

import time 
import orbitPython
import orbitCython
init_time = time.time()
orbitPython.step_time(orbitPython.Planet(),20,10000)
fin_time=time.time()
total_time_python=fin_time - init_time
print("Tiempo total de python: ", total_time_python)

init_time=time.time()
orbitCython.step_time(orbitCython.Planet(),20,10000)
fin_time=time.time()
total_time_cython=fin_time - init_time
print("Tiempo total cython ", total_time_cython)
 
