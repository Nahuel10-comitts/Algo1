/* 
	Escribir una funcion que reciba como parametro una cadena de caracteres
y devuelva la cantidad de digitos numericos que hay en la cadena
*/

#include <stdio.h>
#include <string.h>


int contar_numeros(char cadena[])
{
	int pos = 0, cant_nros = 0;
	
	while (cadena[pos] != '\0')
	{
		if (cadena[pos] >= '0' && cadena[pos] <= '9')
			cant_nros += 1;
		
		pos += 1;
	}
	
	return cant_nros;
}

void main()
{
	char cadena_prueba [] = "65mul80¡0";
	printf("%s %i", cadena_prueba, contar_numeros(cadena_prueba));
	return;
}
