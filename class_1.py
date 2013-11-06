# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:33:17 2013

@author: Mars
"""

class Fruit(object):
	def __init__(self,name,color,taste,poison):
		self.name = name
		self.color = color
		self.taste = taste
		self.poison = poison
		
	def describe(self):
		print "I am %s %s, it tastes %s." % (self.color,self.name,self.taste)
	def is_edible(self):
		if not self.poison:
			print "OK,i am edible"
		else:
			print "Do not eat me!"

apple = Fruit("apple","red","delicious",False)
apple.describe()
apple.is_edible()