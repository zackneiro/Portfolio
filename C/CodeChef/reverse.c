#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_LEN 20

void reverse_word(char *string, int a);

int main(void)
{
    int a = 0;
    char* string = malloc(sizeof(char) * MAX_LEN + 1);

    if (string == NULL)
    {
        printf("Memory allocation failed\n");
        exit(1);
    }

    fgets(string, sizeof string, stdin);

    string[strcspn(string, "\n")] = 0;

    reverse_word(string, a);
    free(string);
    printf("\n");
    return 0;
}

void reverse_word(char *string,  int a)
{

    if (string[a] == '\0')
    {
        return;
    }
    
    reverse_word(string, a + 1);

    printf("%c", string[a]);
}