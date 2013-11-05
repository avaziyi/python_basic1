# -*- coding: utf-8 -*-
def Max(a,b):
	if a>b:
		print a,'is the max'
	else:
		print b,'is the max'
		
x = 5
y = 7
Max(x,y)

print '\n--------local--------------------\n'

def func(x):
	#global x
	print 'x is',x
	x = 20
	print 'Changed local x to',x
	
x = 50
func(x)
print 'x is',x


print '\n--------global--------------------\n'

def func2():
	global x
	print 'x is',x
	x = 20
	print 'Changed local x to',x
	
x = 50
func2()
print 'x is',x

print '\n--------return--------------------\n'
def max(x,y):
	
	'''Prints the max of two numbers
	
	The two values must be integers'''
	x = int(x)
	y = int(y)
	if x > y:
		return x
	else:
		return y

print max(2,3)
print max.__doc__
def somuFunc():
	pass