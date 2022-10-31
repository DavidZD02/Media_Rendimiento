cdef extern from "math.h":
    double sqrt(double x)

cdef class Planet(object):
    cdef public double x, y, z, vx, vy, vz, m

    def __init__(self):
        # Posicion Inicial y velocidad incial    
        self.x = 1.0
        self.y = 0.0
        self.z = 0.0
        self.vx = 0.0
        self.vy = 0.5
        self.vz = 0.0
        self.m = 1.0

cdef void single_step(Planet planeta, double dt):
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


cdef void step_time(planeta, time_span, int n_steps):
    cdef double dt
    cdef int j
    dt = time_span / n_steps
    for j in range(n_steps):
        single_step(planeta, dt)