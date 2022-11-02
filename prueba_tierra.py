"""
Fecha: 2 Noviembre-2022
Autor: David Santiago Zárate Diaz
Tema: Cython
Topico: Planetas orbita gravitacional
Principal: 
"""

import time
import py_orbita
import cy_orbita

"""Ejemplo usando datos del planeta tierra"""
tierraPy = py_orbita.Planet()
tierraPy.x = 100*10**3
tierraPy.y = 300*10**3
tierraPy.z = 700*10**3
tierraPy.vx = 2.000*10**3
tierraPy.vy = 29.87*10**3
tierraPy.vz = 0.034*10**3
tierraPy.m = 5.9741*10*24


"""Ejemplo usando datos del planeta tierra"""
tierraCy = cy_orbita.Planet()
tierraCy.x = 100*10**3
tierraCy.y = 300*10**3
tierraCy.z = 700*10**3
tierraCy.vx = 2.000*10**3
tierraCy.vy = 29.87*10**3
tierraCy.vz = 0.034*10**3
tierraCy.m = 5.9741*10*24

time_span = 400
n_steps = 2000000

formato_datos = "{:.5f},{:.5f}\n"

for i in range(2):
	inicioPy = time.time()
	py_orbita.step_time(tierraPy, time_span, n_steps)
	finalPy = time.time() - inicioPy
	
	inicioCy = time.time()
	cy_orbita.step_time(tierraCy, time_span, n_steps)
	finalCy = time.time() - inicioCy
	
	with open("tierra.csv","a") as archivo:
		archivo.write(formato_datos.format(finalPy, finalCy))
	
	
