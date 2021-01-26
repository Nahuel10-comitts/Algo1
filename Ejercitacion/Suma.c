#include <stdio.h>

void main()
{
	printf("Resultado de la suma: %i\n", suma(2, 3));
	printf("Resultado de la resta: %i\n", resta(3,7));
	printf("Resultado de la multiplicacion: %i\n", multiplicacion(7, 9));
	
	return;
}

int suma(int a, int b)
{
	return a + b;
}
	
int multiplicacion(int a, int b)
{
	return a*b;
}

int resta(int a, int b)
{
	return suma(a, -b);
}
