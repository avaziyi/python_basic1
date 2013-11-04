# -*- coding: utf-8 -*-
poem = '''\
Programming is fun
When the work is done

if you wanna make your work also fun:
	use Python!
'''
f = file('poem.txt','w')
f.write(poem)
f.close

f = file('poem.txt')
while True:
	line = f.readline()
	print "size:", len(line)," ",
	if len(line) == 0:
		break
	print line,

f.close()

#储存器
import cPickle as p

shoplistfile = 'shop.data'

shoplist = ['apple','mango','carrot']

f = file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = p.load(f)
print storedlist