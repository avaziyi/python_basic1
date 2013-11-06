# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:57:30 2013

@author: Mars
"""

class Animal(object):
	is_alive = True
	health = "good"
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# Add your method here!
	def description(self):
		print "%s,%s" % (self.name,self.age)
hippo = Animal("ava",1)
print hippo.description()
print hippo.health
sloth = Animal("z",2)
print sloth.health
ocelot = Animal("y",3)
print ocelot.health