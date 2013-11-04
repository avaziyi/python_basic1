# -*- coding: utf-8 -*-
from time import time
 
def Sub1():
    s1='sda2'
    s2=('sdas','abcd','sd11','gfds')
    t=time()
    result=[]
    for s2_temp in s2:
        c_temp=zip(s1,s2_temp)
        i=0
        for temp in c_temp:
            if temp[0]==temp[1]:
                i+=1
        result.append(i)
    print result
    return time()-t
 
def Sub2():
    s1='sda2'
    s2=('sdas','abcd','sd11','gfds')
    t=time()
    result=[]
    for s2_temp in s2:
        i=0
        for (temp1,temp2) in zip(s1,s2_temp):
            if temp1==temp2:
                i+=1
        result.append(i)
    print result
    return time()-t
 
def Sub3():
    s1='sda2'
    s2=('sdas','abcd','sd11','gfds')
    t=time()
    temp=[int(temp1==temp2) for s2_temp in s2 for (temp1,temp2) in zip(s1,s2_temp)]
    result=[sum(temp[4*i:4*i+4]) for i in range(len(s2))]
    print result
    return time()-t
 
if __name__=='__main__':
    print 'Sub1():',Sub1()
    print 'Sub2():',Sub2()
    print 'Sub3():',Sub3()
