#include <unistd.h>

int     main(int ac, char **av)
{   
    (void)av;
    (void)ac;
    if (ac == 1)
    {
       write(1, "a\n", 2);
       return (1);
    }
    write(1, "a\n", 2);
    return (0);
}