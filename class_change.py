# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:28:40 2013

@author: Mars
"""

class Car(object):
	condition = "new"
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg   = mpg
	def display_car(self):
		return "This is a %s %s with %s MPG." % (self.color,self.model,str(self.mpg))
	def drive_car(self):
		self.condition = "used"

class ElectricCar(Car):
	def __init__(self, model, color, mpg, battery_type):
		self.model = model
		self.color = color
		self.mpg   = mpg
		self.battery_type = battery_type
	#def drive_car(self):
	#	self.condition = "like new"
								
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

my_car2 = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car2.condition
my_car2.drive_car()
print my_car2.condition