#include <unistd.h>
#include <string.h>

int main(void)
{
    char* string_1 = "Hello, world!\n";
    char* string_2 = "My name is Zack!\n";
    char* string_3 = "This is write()!\n";

    size_t string_size = 0;

    char* buffer[] = {string_1, string_2, string_3};

    for (int i = 0; i < 3; i++)
    {   
        string_size = strlen(buffer[i]);
        write(1, buffer[i], string_size);
    }

    return 0;
}