# -*- coding: utf-8 -*-
x = set("spam")
y = set(['h','a'])
y.add('m')
y.add('m')
print x,y
print x&y
print x|y
print x-y

print '\n______________________\n'
#字典转化为list
a = {3:'c',2:'b',1:'a'}
print 'a is:',a
print 'sorted a is:',sorted(a)
b = set(a)
print 'set a is:',b
print 'sorted b is:',sorted(b)

c = set(a.values())
print 'set a.values is:',c
print 'sorted c is:',sorted(c)
