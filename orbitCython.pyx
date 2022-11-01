"""
 * Fecha: 31-Octubre-2022
 * Autor: Yeison Lizcano
 * Materia: Parallel and Distributed Computing
 * Tema: cython
"""

from math import  sqrt 

class Planet(object):
   def __init__(self):
       #some initial positition and velocity
       self.x = 1.0
       self.y = 0.0
       self.z = 0.0
       self.vx = 0.0
       self.vy = 0.5
       self.vz = 1.0
	
       # some mass
       self.m = 1.0
	
def single_step(planet,float dt):
    """Make a single time step"""
  	
    #compute force: gravity towards orig
    cdef float distance = sqrt(planet.x**2+planet.y**2+planet.z**2)
    cdef float Fx = -planet.x/distance**3
    cdef float Fy = -planet.y/distance**3
    cdef float Fz = -planet.z/distance**3
	
    #time step position, acording to velocity
    planet.x+=dt * planet.vx
    planet.y+=dt * planet.vy
    planet.z+=dt * planet.vz	
	
    #time step velocity, acording to force and mass
    planet.vx += dt*Fx/planet.m
    planet.vy += dt*Fy/planet.m
    planet.vz += dt*Fz/planet.m
    
	
def step_time (planet,int time_span,int n_steps):
	
    """Make a number of time steps forward"""	
    cdef int j
    cdef float dt=time_span/n_steps
	
    for j in range(n_steps):
       single_step(planet,dt);


    
