"""
 * Fecha: 28-Octubre-2022
 * Autor: Yeison Lizcano
 * Materia: Parallel and Distributed Computing
 * Tema: Funciones python para el calculo del area bajo la curva trapasoidal
"""

import time 
import orbita.pyx
init_time = time.time()
print("calculo con python: ",orbita.py(400))
fin_time=time.time()
total_time_python=fin_time - init_time
print("Tiempo total de python: ", total_time_python)

init_time=time.time()
print("Calculo con cython: ",orbita.pyx(400))
fin_time=time.time()
total_time_cython=fin_time - init_time
print("Tiempo total cython ", total_time_cython)
print(f"cython es {total_time_python/total_time_cython}")
 
