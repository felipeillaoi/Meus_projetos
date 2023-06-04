#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>
#include <locale.h>
#include <math.h>
#define p printf
#define s scanf

int insira(){
int num;
p("\n\tInsira um Número inteiro:\n\t");
	s("%d",&num);
	return num;
}

int resposta(int a)
{
int b = 0,i;
	for (i = 1;i <= a;i++){
		if(a % i == 0)
		{
		b++;
		}
	}
	return b;
}

void main()
{
int l;for(l = 1; l <= 100; l++)
{
if (l % 5 == 0)
{
p("\n");
}
p("%d ",l);}
setlocale(LC_ALL,"PORTUGUESE");
//system("cls");
int numero,resultado;
numero = insira();
resultado = resposta(numero);
if (resultado == 2){
p("\n\tO Número escolhido é Primo\n\t");	
}else{
p("\n\tO Número escolhido Não é Primo\n\t");
}
p("\n");
system("PAUSE");
main();


}

