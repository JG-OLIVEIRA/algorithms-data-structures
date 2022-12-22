#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    char data;
    struct node *pNext;
} node;

node *init();

void removePosition(int position);

void print();