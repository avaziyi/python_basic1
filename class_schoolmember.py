# -*- coding: utf-8 -*-
"""
Created on Sat Jun 01 16:26:46 2013

@author: Mars
"""

class SchoolMember:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print '(Initialized member: %s)' % self.name
	
	def tell(self):
		print 'Name:%s Age:%s' % (self.name,self.age),

class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print '(Initialized Teacher: %s)' % self.name
	
	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: %d' % self.salary

class Student(SchoolMember):
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print '(Initialized Studeng: %s)' % self.name
	
	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: %s' % self.marks

t = Teacher('Mrs. Shri',40,30000)
s = Student('Swar',22,75)

print 

members = [t,s]
for member in members:
	member.tell()