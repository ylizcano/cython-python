"""
 * Fecha: 28-Octubre-2022
 * Autor: Yeison LIzcano
 * Materia: Parallel and Distributed Computing
 * Tema: cython
"""
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("orbit.pyx"))

setup(ext_modules = exts)
