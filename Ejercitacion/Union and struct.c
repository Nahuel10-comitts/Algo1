#include <stdio.h>
#include <string.h>

/* define simple structure */
struct
{
	unsigned int widthValidated;
	unsigned int heightValidated;
}status1;

/* define a structure with bit fields */
struct 
{
	unsigned int widthValidated: 1;
	unsigned int heightValidated: 1;
}status2;

struct
{
	unsigned int age: 3;
}Age;

/*union Data
{
    int i;
    float f;
    char str[20];
};*/ 

void main()
{
    /*union Data data; 
    data.i = 10;
    printf("data.i: %d\n", data.i);
    
    data.f = 18.67;
    printf("data.f: %f\n", data.f);
    
    strcpy(data.str, "C programming");
    printf("data.str: %s\n", data.str);
    */
    Age.age = 4;
    printf("Sideoz(Age): %d\n",sizeof(Age));
    printf("Age.age: %d\n",Age.age);
    
    Age.age = 7;
    printf("Age.age: %d\n",Age.age);
    
    Age.age = 8;
    printf("Age.age: %d\n", Age.age);
    
    printf("Memory size ocuppied by status1: %d\n", sizeof(status1));
	printf("Memory size ocuppied by status2: %d\n", sizeof(status2));
	
    return;
}
