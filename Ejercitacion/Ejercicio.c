/*Escribir un programa modular, que solicite el ingreso de dos valores,
validando que el primero este entre 0 y 50; y el segundo entre el
primero y 100. Luego intercambie el valor de las variables, mediante el uso
de una funcion desarrollada a tal fin.
Muestre el valor de ambas variables, antes, y despues del intercambio.*/

# include <stdio.h>

int leer_valor(int min, int max)
{
	int valor;
	scanf("%i", &valor);
	
	while(valor < min || valor > max)
	{
		printf("Valor invalido. Reingrese valor entre %i y %i: ", min, max);
		scanf("%i", &valor);
	}
	
	return valor;
}

void intercambiar(int *A, int *B)
{
    int C = *A;
    *A = *B;
    *B = C;
    
    return;
}

unsigned long long factorial(int numero)
{
	int contador;
	
	unsigned long long resultado = 1;
	
	for(contador = 2; contador <= numero; contador += 1)
		resultado *= contador;
		
	
	return resultado;
}

void main()
{
	int A;
	int B;
	
	printf("Calcular el factorial del primer valor: ");
	A = leer_valor(0,50);
	
	printf("Calcular el factorial del segundo valor: ");
	B = leer_valor(0,100);
	
	printf("\nPrimer valor = %i, segundo valor = %i\n", A, B);
	
	intercambiar(&A, &B);
	
	printf("Primer valor = %i, segundo valor = %i\n", A, B);
	
	printf("\nResultado del primer valor: %llu \n", factorial(A));
	printf("Resuldado del segundo valor: %llu \n", factorial(B));
	//system("pause");
	
	return;
}

