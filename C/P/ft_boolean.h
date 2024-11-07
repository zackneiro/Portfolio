#ifndef FT_BOOLEAN_H
#define FT_BOOLEAN_H

#include <unistd.h>
#include <stdbool.h>

#define TRUE 1
#define FALSE 0

typedef int t_bool;

extern int number;
extern const char *EVEN_MSG;
extern const char *ODD_MSG;
extern int SUCCESS;

t_bool ft_is_even(int nbr);
void ft_putstr(char *str);

#endif