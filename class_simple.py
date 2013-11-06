# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:14:23 2013

@author: Mars
"""

class Person(object):
	def __init__(self,name):
		self.name = name
	def sayHi(self):
		print "Hello, how are you?",self.name
		
p = Person('Avaziyi')
p.sayHi()