#include <unistd.h>

int main(int ac, char **av)
{
    if (ac != 2)
    {
        write(1, "\n", 1);
        return (1);
    }
    char    *str;

    str = av[1];
    int i = 0;
    while (str[i] == ' ' || str[i] == '\t')        
            i++;
    while (str[i] != '\0' && str[i] != ' ' && str[i] != '\t')
    {
        write(1, &str[i], 1);
        i++;
    }
    write(1, "\n", 1);
    return (0);    
}