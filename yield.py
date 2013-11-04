# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:33:18 2013

@author: Mars
"""

def gen():
	print 'enter'
	yield 2
	print 'next'
	yield 3
	print 'next again'
for i in gen():
	print i
'''
当下一个for的之后程序接着往下执行到yeild 2。程序停止执行，然会返回一个值“2”。但是还有一个问题就是，最后yield下面的"next again" 会打印出来呢？这也可能就是在执行完最后一个yield 的时候，for i in gen()的时候, 发生了一些什么动作，导致最后一个yield后面的代码也被执行了。
'''	
print '\n______________________\n'
def gen2():
	print 'enter'
	yield 1
	print 'next'
	return 
	print 'next 2'
	yield 2
	print 'next 3'
for i in gen2():
	print i
'''
看明白了这就是yield和return的区别。yield可以向下运行。而return返回后这个函数余下的部分就不能执行了。
'''	