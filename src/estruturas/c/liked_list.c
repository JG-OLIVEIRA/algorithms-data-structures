#include "./liked_list.h"

node *leftStart;

void initList()
{
    leftStart = NULL;
}

int isEmpty()
{
    if (leftStart == NULL)
        return 1;
    return 0;
}

void addValue(int value)
{
    node *aux;
    aux = (node *)malloc(sizeof(node));
    if (aux != NULL)
    {
        aux->value = value;
        aux->pNext = leftStart;
        leftStart = aux;
    }
}

void forEach()
{
    if (!isEmpty())
    {
        node *aux;
        aux = leftStart;
        while (aux)
        {
            printf("[%d]", aux->value);
            aux = aux->pNext;
        }
    }
    else
    {
        printf("\nList is empty!\n");
    }
}

void removeValue(int value)
{
    node *pBefore = NULL;
    node *aux = leftStart;
    if (!isEmpty())
    {
        while ((aux != NULL) && (aux->value != value))
        {
            pBefore = aux;
            aux = aux->pNext;
        }
        if (aux == NULL)
        {
            printf("Not found for value '%d'", value);
        }
        else
        {
            if (pBefore == NULL)
                leftStart = aux->pNext;
            else
                pBefore->pNext = aux->pNext;
            free(aux);
        }
    }
    else
        printf("Empty list!");
}

int main(void)
{

    int op, value, stop;

    stop = 1;

    initList();

    while (stop)
    {
        printf("\n1 - Inserir");
        printf("\n2 - Exibir a lista");
        printf("\n3 - Remover elemento");
        printf("\n4 - Sair\n");
        printf("\nOpcao: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("\nDigite um inteiro: ");
            scanf("%d", &value);
            addValue(value);
            break;
        case 2:
            printf("\n");
            forEach();
            printf("\n");
            break;
        case 3:
            printf("\nDigite um elemento para remover da lista: ");
            scanf("%d", &value);
            removeValue(value);
            break;
        case 4:
            stop = 0;
            break;
        }
    }
    return 0;
}
