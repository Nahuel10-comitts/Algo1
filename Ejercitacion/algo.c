
/*http://www.cplusplus.com/reference/cstring/?kw=string.h*/
#define MAX 10
void cargar_vector(int vector[]);
void mostar_vector(int vector[]);
void cadenas();

int main(){
	int vector(MAX);
	cargar_vector(vec);
	mostar_vector(vec);
	/*
	cadena();
	*/
	return 0;
}
void cargar_vector(int vec[]);{
	int i;
	for(i = 0; i < MAX; i++){
		vec[i]= (i + 1)*(i + 1);
	}

}
void mostrar_vector(int vec[]){
	int i;
	for(i = 0; i < MAX; i++){
		printf(" %i \n", vec[i]);
	}
}
