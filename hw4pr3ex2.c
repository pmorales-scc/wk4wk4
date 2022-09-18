// CSCI 1550: HW 3, Problem 5 exercise 2 (PART 2)
// Filename: hw4pr3ex2.c
// Name: Peter Morales
//
// Exercise: Solving the quadratic equation! 

#include <math.h>
#include <stdio.h>

int Discriminant(int a, int b, int c){
    int d;
    d = b*b - 4*a*c;

    return d;
}

int xPlus(int a, int b, int c){
    float xP;

    xP = (-b + sqrt(Discriminant(a, b, c)))/2*a;

    return xP;
}
int xMinus(int a, int b, int c){
    float xM;

    xM = (-b - sqrt(Discriminant(a, b, c)))/2*a;

    return xM;
}

int main() {
    int a;
    int b;
    int c;
    int xP_answ;
    int xM_answ;

    a = 1;
    b = -4;
    c = -12;

    xP_answ = xPlus(a, b, c);
    xM_answ = xMinus(a, b, c);

    printf("%d\n",xP_answ);
    printf("%d\n",xM_answ);

    return 0;
}