"""
Fecha: 2 Noviembre-2022
Autor: David Santiago Zárate Diaz
Programa en Python para el calculo de la raiz
"""

from math import sqrt

class Planet(object):
	def __init__(self):
		# Posicion Inicial y velocidad incial    
		self.x = 1.0
		self.y = 0.0
		self.z = 0.0
		self.vx = 0.0
		self.vy = 0.5
		self.vz = 0.0
		self.m = 1.0

def single_step(planeta, dt):
	distancia = sqrt(planeta.x**2 + planeta.y**2 + planeta.z**2)
	Fx = -planeta.x / distancia**3
	Fy = -planeta.y / distancia**3
	Fz = -planeta.z / distancia**3
	# Time step position, according to velocity
	planeta.x += dt * planeta.vx
	planeta.y += dt * planeta.vy
	planeta.z += dt * planeta.vz
	# Time step velocity, according to force and mass
	planeta.vx += dt * Fx / planeta.m
	planeta.vy += dt * Fy / planeta.m
	planeta.vz += dt * Fz / planeta.m


def step_time(planeta, time_span, n_steps):
	dt = time_span / n_steps
	for j in range(n_steps):
		single_step(planeta, dt)
