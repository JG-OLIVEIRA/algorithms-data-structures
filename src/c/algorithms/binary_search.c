#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *vector, random_number, found_number, vector_size;

    printf("\n");
    printf("Tell a size of the vector: ");
    scanf("%d", &vector_size);
    printf("\n");

    vector = (int *)malloc(sizeof(int) * vector_size);

    if (vector == NULL)
    {
        printf("Fail to allocate memory");
    }

    for (int index = 0; index < vector_size; index++)
    {
        vector[index] = rand() % (index + 1);
    }

    print_vector(vector, vector_size);

    printf("\n");
    printf("Input a number that you want to know the index: ");
    scanf("%d", &random_number);
    printf("\n");

    printf("\n");
    printf("Trying to find '%d'...\n", random_number);
    found_number = binary_search(vector, random_number, 0, vector_size);

    if (found_number != -1)
    {
        printf("Element position: %d\n", found_number);
    }
    else
    {
        printf("Not found for element '%d'", random_number);
    }

    printf("\n");

    return EXIT_SUCCESS;
}

int binary_search(int *vector, int key, int min, int max)
{
    if (min <= max)
    {
        int middle = (min + max) / 2;

        if (key == vector[middle])
            return middle;
        else if (key < vector[middle])
            return binary_search(vector, key, min, middle - 1);
        else if (key > vector[middle])
            return binary_search(vector, key, middle + 1, max);
    }

    return -1;
}

void print_vector(int *vector, int vector_size)
{
    for (int i = 0; i < vector_size; i++)
    {
        printf("[%d] ", vector[i]);
    }
}