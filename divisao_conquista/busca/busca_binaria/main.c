#include <stdio.h>
#include <stdlib.h>

int busca_binaria(int *array, int key, int min, int max)
{
    if (min <= max)
    {
        int middle = (min + max) / 2;

        if (key == array[middle])
            return middle;
        else if (key < array[middle])
            return busca_binaria(array, key, min, middle - 1);
        else if (key > array[middle])
            return busca_binaria(array, key, middle + 1, max);
    }

    return -1;
}

int main()
{
    int vetor[] = {1, 2, 3, 4, 5};

    int valoresProcurados[] = {3, 4, 6};

    size_t n = sizeof(valoresProcurados) / sizeof(int);

    for (int i = 0; i < n; i++)
    {
        int elemento = valoresProcurados[i];

        int resultado = busca_binaria(vetor, elemento, 0, n - 1);

        if (resultado == -1)
        {
            printf("\nElemento %d não encontrado", elemento);
        }
        else
        {
            printf("\nElemento %d na posição %d", elemento, resultado);
        }
    }
}