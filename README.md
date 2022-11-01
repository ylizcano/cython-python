# Introducción
**Cython**
- Es un lenguaje de programación que combina Python con el sistema
  de tipos estáticos de C y C++.
- Es un compilador que traduce el código fuente de Cython a un código fuente C o C++ eficiente.
  Este código fuente se puede compilar en un módulo de extensión de Python o en un ejecutable      
  independiente.


## Instalación

Se utiliza el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar cython,
y para la compilación se utiliza el comando:

```bash
pip install cython
python3 setup.py build_ext --inplace

