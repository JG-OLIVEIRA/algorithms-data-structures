#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int value;
    struct node *pNext;
} node;

void initList(void);

int isEmpty(void);

void forEach(void);

void addValue(int value);

void removeValue(int value);