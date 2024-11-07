#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int main (void)
{
    

    char number = 55;

    write(1, &number, 1);
    write(1, "\n", 1);

    return 0;
}