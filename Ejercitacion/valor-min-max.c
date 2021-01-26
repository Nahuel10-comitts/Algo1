/* Ejemplo: Solicitar el ingreso de un valor, asegurando que este entre un minimo y un maximo.
*/

#include <stdio.h>

#define MIN 0
#define MAX 100

int main() {
    int valor;
    
    do {
        printf("Ingrese un número: ");
        scanf("%d", &valor);
    } while (valor < MIN || valor > MAX);
    
    printf("Gracias, elegiste un número válido!");
    printf("%d está entre %d y %d", valor, MIN, MAX);
    
    return 0;
}