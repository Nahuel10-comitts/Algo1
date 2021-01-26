#include <stdio.h>
#include <string.h>

char *string_dinamico;
int largo_actual = 0;
int delta_incremento = 100;
char buffer_lectura[50];

string_dinamico = (char*) malloc(delta_incremento * sizeof(char));
string_dinamico[0] = '\0';

largo_actual = delta_incremento;

do{
	printf("\nIngrese un texto:\n");
	scanf("%s",buffer_lectura);
	
	if(strlen(buffer_lectura) + strlen(string_dinamico) > largo_actual){
		string_dinamico = (char*) realloc(string_dianmico, (largo_actual + delta_incremento) * sizeof(char));
		largo_actual += delta_incremento;
	}
	strcat(string_dinamico, buffer_lectura);
} while(strlen(buffer_lectura) > 0);
	printf("Todo lo ingresado fue: %s", string_dinamico);
	
