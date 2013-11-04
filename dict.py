# -*- coding: utf-8 -*-
ab = {'ava':'lzy@163.com','yu':'yu@126.com','mars':'j@c.com'}
print "My contact ava's address is %s"%ab['ava']
ab['sun'] = 'orz@z.c'
#del ab['sun']
print 'there are %d contacts in the Contact'%len(ab)
for name,address in ab.items():
	print 'Contact %s at %s' %(name,address)
	
#等价
for i in ab.keys():
	print 'First Method:the address is %s'%ab[i]
for j in ab.values():
	print 'Second Method:the address is %s'%j
#if 'ava' in ab:# OR 
if ab.has_key('ava'):
	print "ava's address is %s"%ab['ava']
	
print '\n______________________________________\n'
