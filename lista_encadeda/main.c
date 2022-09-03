#include <stdio.h>
#include <stdlib.h>

typedef struct no
{
  int info;
  struct no *prox;
} no;

no *inicioL;

void iniciaLista()
{
  inicioL = NULL;
}

int listaVazia()
{
  if (inicioL == NULL)
    return 1;
  return 0;
}

void insereValor(int valor)
{
  no *aux;
  aux = (no *) malloc (sizeof (no));
  if (aux != NULL)
    {
      aux->info = valor;
      aux->prox = inicioL;
      inicioL = aux;
    }
}

void percorreLista()
{
  if (!listaVazia())
    {
      no *aux;
      aux = inicioL;
      while (aux)
	    {
	        printf ("[%d]", aux->info);
	        aux = aux->prox;
	    }
    }
  else
    {
      printf ("\nLista Vazia!\n");
    }
}

int main(){
    
  int op, valor, stop;

  iniciaLista();

  stop = 1;

  while (stop)
    {
        printf ("\n1 - Inserir");
        printf ("\n2 - Exibir a lista");
        printf ("\n3 - Sair\n");

        printf ("\nOpção: ");
        scanf ("%d", &op);

        switch(op)
            {
	            case 1:
	                printf ("\nDigite um inteiro: ");
	                scanf ("%d", &valor);
	                insereValor (valor);
	                break;
	            case 2:
	                printf ("\n");
	                percorreLista ();
	                printf ("\n");
	                break;
	            case 3:
	                stop = 0;
	                break;
            }
	 }
  return 0;
}
