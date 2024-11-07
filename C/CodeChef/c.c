#include <stdio.h>
#include <stdbool.h>

bool is_there_number(int target, int array_size, int array[]);
int get_number(const char* text);

int main(void)
{   
    int target = 0;
    int array[] = {1, 2, 3, 4, 5};
    int array_size = sizeof(array) / sizeof(array[0]);
    target = get_number("Please provide us with a number you are looking for: ");

    if (target == -1)
    {
        printf("Invalid input. Exiting...\n");
        return 1;
    }
       

    if (is_there_number(target, array_size, array))
    {
        printf("Found\n");
        return 0;
    }

    else
    {
        printf("Not found. Exiting...\n");
        return 1;
    }
}


int get_number(const char* text)
{
    int number = 0, scan_result = 0;

    printf("%s", text);
    scan_result = scanf("%d", &number);

    if (scan_result != 1)
    {
        return -1;
    }
    return number;
}

bool is_there_number(int target, int array_size, int array[])
{

    for (int i = 0; i < array_size; i++)
    {
        if (array[i] == target)
        {
            return true;
        }
    }
    return false;
}
