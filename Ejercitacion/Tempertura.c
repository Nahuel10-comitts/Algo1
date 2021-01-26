#include <stdio.h>
#include <string.h>

int temp;
char grado;
float prom;
char mes[15];

/*int temp = 25;
char grado = 'C';
float prom = 20.5;
char mes[15] = "Marzo";
*/
void main()
{
	printf("Ingrese la temperatura,grado, promedio de temperaturas y el mes separados por espacios\n");
	scanf("%d %c %f %s", &temp, &grado, &prom, mes);
	
	//printf("La temperatura hoy es: %d°%c, el promedio fue de: %f en todo el mes de: %s\n", temp, grado, prom, mes);
}

