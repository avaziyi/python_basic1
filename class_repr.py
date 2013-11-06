# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:42:57 2013

@author: Mars
"""

class Point3D(object):
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def des(self):
		print "the points are %s %s %s" % (self.x,self.y,self.z)
	def __repr__(self):
		print "(%s, %s, %s)" % (self.x,self.y,self.z)
my_point = Point3D(1,2,3)
my_point.des()
my_point.__repr__()