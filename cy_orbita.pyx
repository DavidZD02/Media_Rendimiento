#cython: language_level=3

cimport cython

"""
Fecha: 2 Noviembre-2022
Autor: David Santiago Zárate Diaz
Programa en Cython para el calculo de la raiz
"""

cdef extern from "math.h":
	double sqrt(double x) nogil

cdef class Planet(object):
	"""Declaracion de tipo de datos publica"""	
	cdef public double x, y, z, vx, vy, vz, m
	
	def __init__(self):
		self.x = 1.0
		self.y = 0.0
		self.z = 0.0
		self.vx = 0.0
		self.vy = 0.5
		self.vz = 0.0
		self.m = 1.0

@cython.cdivision(True)
cdef void single_step(Planet planeta, double dt) nogil:
	cdef double distancia, Fx, Fy, Fz
	distancia = sqrt(planeta.x**2 + planeta.y**2 + planeta.z**2)
	Fx = -planeta.x / (distancia**3)
	Fy = -planeta.y / (distancia**3)
	Fz = -planeta.z / (distancia**3)
	# Time step position, according to velocity
	planeta.x += dt * planeta.vx
	planeta.y += dt * planeta.vy
	planeta.z += dt * planeta.vz
	planeta.vx += (dt*Fx)/planeta.m
	planeta.vy += (dt*Fy)/planeta.m
	planeta.vz += (dt*Fz)/planeta.m

def step_time(Planet planeta, float time_span, int n_steps):
	cdef float dt
	cdef int j
	dt = time_span / n_steps
	"""Habilitar la posibilidad de paralelismo"""
	with nogil:
		for j in range(n_steps):
			single_step(planeta, dt)
