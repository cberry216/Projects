"""satellite.py - module to house the class for a satellite for any
planet in the solar system"""

from planets import Planets
import math 

def degrees_to_radians(degrees):
	return degrees * math.pi / 180

class Satellite:
	"""Class to represent a satellite orbiting a particular planet"""

	def __init__(self, radius, velocity, elevation_angle=0, inclination,
				 planet=Planets.Earth):
		"""
		__init__: constructor for Satelliate object
		Parameters:
			radius: radius at which satellite orbits planet in m
			velocity: velocity at which satellite is travelling in m/s
			elevation_angle: position in orbit where satellite is
				is currently located in degrees (default is it 
				periapsis)
			inclination: inclation of satellite's orbit in degrees
			planet: planet which satellite is orbiting (default is
				planet Earth)
		"""
		self.radius = radius
		self.velocity = velocity
		self.elevation_angle = elevation_angle
		self.inclination = inclination
		self.planet = planet
		# Following members are calcluated using the get methods

	def get_angular_momentum(self):
