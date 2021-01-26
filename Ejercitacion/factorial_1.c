/* 
Escribir un programa modular que solicite el ingreso
de un valor, validando que el mismo este entre 0 y 20;
y luego calcule e informe el factorial del numero ingresado.
Si el numero ingresado no cumple con lo solicitado, informar
y pedir el reingreso del numero.Repetir la operacion hasta
que el numero sea valido.*/

# include <stdio.h>

int leer_valor(int min, int max)
{
	int n;
	scanf("%i", &n);
	
	while(n < min || n > max)
	{
		printf("Valor invalido. Reingrese valor entre %i y %i: ", min, max);
		scanf("%i", &n);
	}
	
	return n;
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
	int n;
	printf("Calcular el factorial de: ");
	n = leer_valor(0,20);
	
	printf("\nResultado: %llu \n", factorial(n));
	
	//system("pause");
	
	return;
}
