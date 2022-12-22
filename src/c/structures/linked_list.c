#include "linked_list.h"

node *head;
node *tail;

node *init()
{
    head = (node *)malloc(sizeof(node));
    head->data = 'A';

    node *nodeB = (node *)malloc(sizeof(node));
    nodeB->data = 'B';
    head->pNext = nodeB;

    node *nodeC = (node *)malloc(sizeof(node));
    nodeC->data = 'C';
    nodeB->pNext = nodeC;

    tail = (node *)malloc(sizeof(node));
    tail->data = 'D';
    nodeC->pNext = tail;
    tail->pNext = NULL;

    return head;
}

void removePosition(int position)
{
    node *p = head;
    int i = 0;

    while (p->pNext && i < position - 1)
    {
        p = p->pNext;
        i++;
    }

    node *temp = p->pNext;
    p->pNext = p->pNext->pNext;
    temp->pNext = NULL;
}

void print()
{   
    node *p = head;
    while (p)
    {
        printf("[%c] -> ", p->data);
        p = p->pNext;
    }
    printf("End\n\n");
}

int main(void)
{   
    init();
    removePosition(2);
    print();

    return 1;
}