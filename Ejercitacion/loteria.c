 /* El uso del condicional "if", dependiendo de lo que debamos resolver, 
   puede ser:
      simple: sin rama "else"
      compuesto: con rama "else"
      anidado: cuando ya sea por la rama verdadera o falsa, encontramos otro "if".

   En este ejemplo lo usaremos "simple".
   
Ejemplo: Solicita el ingreso de un numero y lo compara contra un valor establecido 
*/

#define LOTERIA 42

int main()
{
    int valor; //declarar
    
    printf("Ingrese un valor a comparar: ");
    scanf("%d", &valor);
    
    if (valor == LOTERIA) 
       printf("Ganaste!!!\n");
    else
       printf("Segui participando.\n");
       
    printf("Chau!");
    
    return 0;
}
