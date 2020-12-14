#include <stdio.h>
#include <math.h>
#define LIMITE 1000

int main(){
    int potencia  = 2;
    int exponente = 0;
    int resultado = pow(2,0);

    while (resultado < LIMITE){
        printf("Potencia de %d elevado a %d es %d  \n", potencia, exponente, resultado);
       	exponente++;
        resultado = pow( potencia, exponente);
	    
    
    }
    return 0;
}
