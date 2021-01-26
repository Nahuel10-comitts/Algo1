/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
/* Comentario de 1 línea */
// C99 incorpora el comentario hasta fin de línea, equivalente al # de Python
#include <stdio.h> // stdio == STandard Input Output (Entrada/Salida Estándar)

#define PI 3.1416 // C es "case sensitive"
#define NOMBRE "Ezequiel"

typedef char tCantDiasMes;

int main()
{
    int a;
    unsigned int b = 0;
    long int c;
    signed short int d;
    tCantDiasMes t_cant_dias_mes;
    const float Pi = 3.14;
    
    float radio = 3.22;
    a = PI * radio * radio;
    
    printf("Tama�oo de Pi: %d, tama�o del float: %d\n", sizeof(Pi), sizeof(float));
    printf("Valor de Pi: %f\n", Pi);
    printf("Valor de PI: %f\n", PI);
    
    printf("Nombre: %f\n", NOMBRE);
    
    return 2;
}
