// CSCI 1550: HW 4, Problem 3 exercise 1 (PART 1)
// Filename: hw4pr2ex1.c
// Name: Peter Morales
//
// Exercise: Actually planning the 4 4s challenge!

#include <math.h>
#include <stdio.h>

int main() {
    int a, b, c, d, e, f, g;
    
        a = (sqrt(4) + sqrt(4) + 4 - 4); // four
        b = 4*4/4*4; //sixteen
        c = sqrt(4) + sqrt(4) + sqrt(4) + 4; //ten
        d = 4 * 4 - 4*1; //twelve
        e = 4/4 + sqrt(4) + sqrt(4); // five
        f = 4 * sqrt(4) + 4/4; //nine
        g = 4/4 + 4 + sqrt(4); // seven

        printf("In C, four is: %d\n",a);
        printf("In C, five is: %d\n",e);
        printf("In C, seven is: %d\n",g);
        printf("In C, nine is: %d\n",f);
        printf("In C, ten is: %d\n",c);
        printf("In C, twelve is: %d\n",d);
        printf("In C, sixteen is: %d\n",b);
        


    return 0;
}

