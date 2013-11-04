# -*- coding: utf-8 -*-
st = "Python Is A Great Programming Language!"
for index in range(len(st)): 
	print st[index],

print '\n______________________________________\n'

for s in st:
	print s,

print '\n______________________________________\n'

for item in st.split(' '):
	print item, len(item)

print '\n______________________________________\n'

a = ('first','second','now')
print 'The tuple is',a
print 'The first element is',a[0]
try:
	a.append('change')
except Exception,e:
	print e
print a[0][0]

print '\n______________________________________\n'

b = ['first','second','now']
print 'The original list is',b
print 'The first element is',b[0]
b.append('change')
b[3] = 'changed again'
print 'The new list is',b
#print b[0][0]

print '\n______________________________________\n'
a = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
print a[0][0][1]
print 'The outer tuple is',a,'and length is',len(a)
print 'The middle tuple is',a[0],'and length is',len(a)
print 'The inner tuple is',a[0][0],'and length is',len(a)

print '\n______________________________________\n'
l = [i for i in range(10)]
print l
print id(l)
print l.reverse()
print id(l)
print l.sort()
print id(l)
print l.index(5)
print l.count(0)
#==============================================================================
# append 和 pop 方法对 list 函数的操作要么是先进先出 (FIFO) 数据结构（也称为队列），
# 要么是后进先出 (LIFO) 数据结构（也称为堆栈）。
# 通过允许您将条目设置为从 list 中弹出（删除并返回），pop 方法支持这些功能。
# 如果弹出 list 的第一项，则是一个队列；
# 反之，如果弹出 list 的最后一项，则是一个堆栈。
#==============================================================================
print '\n______________________________________\n'
t = (0,1,2,3,4,5,6,7,8,9)
print t[2]
print (t[0], t[9], t[-1])
print t[2:7]
print t[:]
print t[2:7:2]
print t[2::2]
print t[:-2]

print '\n______________________________________\n'

shoplist = ['apple','mango','carrot','banana']
mylist = shoplist
print 'shoplist is', shoplist
del shoplist[0]
print 'shoplist now is', shoplist
print 'mylist is', mylist

print u'Copy by making a full slice……'
mylist = shoplist[:]
del mylist[0]
print 'shoplist is', shoplist
print 'mylist is', mylist

#向 list 中增加元素
li = ['a', 'b', 'mpilgrim', 'z', 'example']
print li
li.append("new")              
print li
li.insert(2, "new")           
print li
li.extend(["two", "elements"])
print li
print '\n______________________________________\n'

#从 list 中删除元素
li.remove('a')
print li
li.pop()
print li
print '\n______________________________________\n'

#使用join链接list成为字符串
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print ["%s=%s" % (k, v) for k, v in params.items()]
print ";".join(["%s=%s" % (k, v) for k, v in params.items()])
print '\n______________________________________\n'

#分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print s
print s.split(";")   
print s.split(";", 1)
print '\n______________________________________\n'

#列表过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print [elem for elem in li if len(elem) > 1]      
print [elem for elem in li if elem != "b"]        
print [elem for elem in li if li.count(elem) == 1]