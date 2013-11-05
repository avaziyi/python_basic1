# -*- coding: utf-8 -*-
import threading
def sayhello():
	#global t        #Notice: use global variable!
	t = threading.Timer(5.0, sayhello)
	t.start()
	print "hello world"
	
#t = threading.Timer(5.0, sayhello)
#t.start() 

sayhello()