# CSCI 1550: HW 4, Problem 4
# Filename: hw4pr4.py
# Name: Peter Morales
#
# Task 1: 2's complement via "fast operations"

from math import *

def int2int8(n):
    a = (n & 255)
    return a

def add(n1,n2):
    a = int2int8(n2 + n1)
    return a

def neg(n):
    a = add(~(n), 1)
    return a

def sub(n1,n2):
    a = (add(n1,neg(n2))) 
    return a

def divBy2(n):
    a = (n>>1)
    return a

# TASK 2:  Extracting binary-digits!

def mod2(n):
    a = sub((divBy2(n+1)), (divBy2(n)))
    return a

def bit2string(b):
    a = str(b)
    return a

def int8ToString(n):
    a = str((mod2(divBy2(divBy2(divBy2(divBy2(divBy2(divBy2(divBy2(n)))))))))) + str(((mod2(divBy2(divBy2(divBy2(divBy2(divBy2(divBy2(n)))))))))) + str((mod2(divBy2(divBy2(divBy2(divBy2(divBy2(n)))))))) + str(((mod2(divBy2(divBy2(divBy2(divBy2(n)))))))) + str((mod2(divBy2(divBy2(divBy2(n)))))) + str(((mod2(divBy2(divBy2(n)))))) + str((mod2(divBy2(n)))) + str((mod2(n)))
    return a
    
def displayInt8(n):
    a = bit2string(-neg(n))
    b = int8ToString(n)
    print("val:",(a))
    print("bin:",(b))
    None
