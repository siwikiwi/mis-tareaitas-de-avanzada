# Tarea 3

### Referencias que utilice en mi tarea
- Referencias: para instrucciones del reduce utilice reduce(lambda x, y: x + [y], generador) lambda x, y: x if y in x else x + [y], 
extraido desde esta issue del repositorio https://github.com/IIC2233/Syllabus/issues/339

- en pares_candidatos, ocupo combinations de itertools (sugerencia del enunciado) 
https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/

- en animales mas viejos
para obtener los valores del diccionario, fuente: 
https://www.programiz.com/python-programming/methods/dictionary/values

- en edad_pocentaje y edad promedio https://www.geeksforgeeks.org/python-itertools-tee/?ref=header_search referencia de usar iter, tee 

### Librerias 
from typing import Generator
import utilidades #para hacer las namedtuples
from functools import reduce #usar reduce
from os.path import join #crear rutas
from itertools import combinations, tee
from collections import Counter
-
modulo propio mis_funciones.py 
