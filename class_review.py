# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:00:10 2013

@author: Mars
"""

class Triangle(object):
	number_of_sides = 3
	def __init__(self,angle1,angle2,angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3
	def check_angles(self):
		if self.angle1+self.angle2+self.angle3==180:
			#print 'It makes the triangle'			
			return True
		else:
			return False        

class Equilateral(Triangle):
	angle = 60
	def __init__(self):
		self.angle1 = self.angle
		self.angle2 = self.angle
		self.angle3 = self.angle
		
my_triangle = Triangle(60,60,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

equi_triangle = Equilateral()
print equi_triangle.angle
