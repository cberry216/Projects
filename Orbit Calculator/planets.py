""" planets.py - module to house the planet class along with each
planet in the Sol system
"""

from enum import Enum

big_G = 6.67408e-11 #in m^3/(kg s^2)

class Planet:
	"""Class to represent a planet orbiting the Sun """
	
	def __init__(self, mu, radius, semi_maj_axis, r_soi, vel_p, vel_esc):
		"""
		__init__: constructor for Planet object
		Parameters:
			mu: the gravitational parameter of planet in m^3/s^2
			radius: radius of planet in kilometer (this is the distance
					from center of planet to crust)
			semi_maj_axis: semi-major axis of planet in meters
			r_soi: radius of the sphere of influence of planet
			vel_p: velocity of planet in relation to Sun in m/s
			vel_esc: escape velocity from surface of the planet in m/s
		"""
		self.mu = mu
		self.radius = radius
		self.semi_maj_axis = semi_maj_axis
		self.r_soi = r_soi
		self.vel_p = vel_p
		self.vel_esc = vel_esc

###################################################################
#			    			Planet Object                         #
###################################################################
class Planets(Enum):
	Sun 	= Planet(1.327e20, 7.000e8, 0, 0, 0, 0)
	Mercury = Planet(2.168e13, 2.439e6, 0.579e11, 1.117e8, 47870, 4217)
	Venus	= Planet(3.248e14, 6.052e6, 1.082e11, 6.163e8, 35040, 10360)
	Earth	= Planet(3.986e14, 6.378e6, 1.496e11, 9.245e8, 29790, 11180)
	Mars	= Planet(4.297e13, 3.393e6, 2.280e11, 5.178e8, 24140, 5032)
	Jupiter = Planet(1.267e17, 7.140e7, 7.784e11, 4.820e10, 13060, 59568)
	Saturn  = Planet(3.739e16, 6.027e7, 1.434e12, 5.460e10, 9680, 35500)
	Uranus	= Planet(5.794e15, 2.556e7, 2.872e12, 5.180e10, 6800, 21300)
	Neptune = Planet(6.835e15, 2.476e7, 4.495e12, 8.680e10, 5430, 23500)
	Pluto	= Planet(8.700e11, 1.187e6, 5.906e12, 3.291e10, 4670, 1210)