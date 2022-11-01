"""
 * Fecha: 31-Octubre-2022
 * Autor: Yeison Lizcano
 * Materia: Parallel and Distributed Computing
 * Tema: cython
"""
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("orbitCython.pyx"))

setup(ext_modules = exts)
