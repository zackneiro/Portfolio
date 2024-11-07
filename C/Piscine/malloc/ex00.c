#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int     n;
    int     *p;

    n = 5;

    p = (int *) calloc(n, 4);

    if (p == NULL)
    {
        exit(1);
    }   

    for (int i = 0; i < n; i++)
    {
        p[i] = i;
    }

    for (int f = 0; f < n; f++)
    {
        printf("%d, ", p[f]);
    }
    printf("\n");

    n = 11,
    p = (int *)realloc(p, 11 * 4);

    if (p == NULL)
    {
        printf("_NOT_ENOUGH_MEMORY_\n");
        return (1);
    }

    for (int f = 5; f < n; f++)
    {
        p[f] = f;
    }
    for (int c = 0; c < n; c++)
    {
        printf("%d, ", p[c]);
    }

    printf("\n");
    free(p);
    return (0);
}