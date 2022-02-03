#!/usr/bin/env python

##  BGCD.py

import sys
if len(sys.argv) != 3:
    sys.exit("\nUsage:   %s  <integer>  <integer>\n" % sys.argv[0])

a,b = int(sys.argv[1]),int(sys.argv[2])
def bgcd(a,b):
    if a == b:
        print('The MI is 1.') 
        return a                                         #(A)
    if a == 0: 
        print('There is no MI.') 
        return b                                         #(B)
    if b == 0: 
        print('There is no MI.') 
        return a                                         #(C)
    if (~a & 1):                                                #(D)
        if (b &1):                                              #(E)
            return bgcd(a >> 1, b)                              #(F)
        else:                                                   #(G)
            return bgcd(a >> 1, b >> 1) << 1                    #(H)
    if (~b & 1):                                                #(I)
        return bgcd(a, b >> 1)                                  #(J)
    if (a > b):                                                 #(K)
        return bgcd( (a-b) >> 1, b)                             #(L)
    return bgcd( (b-a) >> 1, a )                                #(M)

def mod_mult_inv(a, y):
    x = bgcd(a, y)
    return x % y

mult_inv = mod_mult_inv(a, b)
gcdval = bgcd(a, b)
print("\nBGCD: %d\n" % gcdval)
print("\nMI: %d\n" % mult_inv)
