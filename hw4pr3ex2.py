# CSCI 1550: HW 3, Problem 5 exercise 2 (PART 1)
# Filename: hw4pr3ex2.py
# Name: Peter Morales
#
# Exercise: Solving the quadratic equation!

from math import *

def Discriminant(a, b, c):
    d = b**2 - 4*a*c
    return d

def QuadSolver(a, b, c):
    xPlus = (-b + sqrt(Discriminant(a, b, c)))/2*a
    xMinus = (-b - sqrt(Discriminant(a, b, c)))/2*a
    return [xPlus, xMinus]

a = 1
b = -4
c = -12
d = QuadSolver(a, b, c)

print(d[0])
print(d[1])