#include <ctype.h>
#include <stdio.h>


int scan_num(const char* text);

int main(void)
{
    return 0;
}



int scan_num(const char* text)
{
    int num = 0, scan_result = 0;

    printf("%s", text);

    scan_result = scanf("%d", &num);

    if (scan_result != 1 || scan_result < 0)
    {
        printf("Invalid input. Please try again later\n");
        return 0;
    }
    
    return num;
}