#include "ft_boolean.h"

const char *EVEN_MSG = "I have an even number of arguments.\n";
const char *ODD_MSG = "I have an odd number of arguments.\n";
int SUCCESS = 0;

#define EVEN(number) (number % 2== 0) ? 0: 1

void ft_putstr(char *str)
{
    while (*str)
        write(1, str++, 1);
}

t_bool ft_is_even(int nbr)
{
    return ((EVEN(nbr)) ? TRUE : FALSE);
}

int main(int argc, char **argv)
{
    (void)argv;
    if (ft_is_even(argc - 1) == TRUE)
    {
        ft_putstr(EVEN_MSG);
    }
    else
    {
       ft_putstr(ODD_MSG); 
    }
    return (SUCCESS);
}