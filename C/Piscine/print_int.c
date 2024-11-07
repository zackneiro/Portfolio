#include <unistd.h>

void    write_str(char *str)
{   
    int     len;

    len = 0;
    while(str[len] != '\0')
    {
        len++;
    }
    write(1, str, len);
}

void int_to_str(int num, char *buf)
{
    int     tmp;
    int     len;

    tmp = num;
    len = 0;

    // first, i need to count how many digits I have

    while (tmp != 0)
    {
        len++;
        tmp /= 10; // moving on next digit
    }

    buf[len] = '\0';

    while (len != 0)
    {
        len--;
        buf[len] = (num % 10) + '0';
        num /= 10; // moving on next digit of num
    }
}

int main(void)
{  
    int     num;
    char    buffer[10];

    num = 0;
    while (num <= 100)
    {
        if (num % 4 == 0 && num % 7 == 0)
            write_str("fizzbuzz\n");
        else if (num % 4 == 0)
            write_str("fizz\n");
        else if (num % 7 == 0)
            write_str("buzz");
        else
        {
            int_to_str(num, buffer);
            write_str(buffer);
            write(1, "\n", 1);
        }
        num++;
    }


    return (0);
}