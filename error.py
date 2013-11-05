# -*- coding: utf-8 -*-
import sys
try:
	s = raw_input('Enter something --> ')
except EOFError:
	print '\nWhy did you do an EOF on me?'
	sys.exit()
except:
	print '\nSome error/exception occurred.'

print 'Done'
print '\n____________________\n'
import time

try:
	f = file('poem.txt')
	while True:
		line = f.readline()
		if len(line) == 0:
			break
	time.sleep(2)
	print line,
finally:
	f.close()
	print u'Cleaning up……the file is closed'