#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
    int array[100], total_baz = 0, total_biz = 0, total_biz_baz = 0;
    char output[100];

    for (int i = 0, k = 1; i < 100; i++)
    {
        array[i] = k;
        k++;
    }

    for (int l = 0; l < 100; l ++)
    {
        if (array[l] % 3 == 0 && array[l] % 5 == 0)
        {
            write(1,"biz-baz\n", 8);
            total_biz_baz++;
        }
        else if (array[l] % 3 == 0)
        {
            write(1, "biz\n", 4);
            total_biz++;
        }
        else if (array[l] % 5 == 0)
        {
            write(1,"baz\n", 4);
            total_baz++;
        }
    }

    snprintf(output, sizeof(output), "Total biz-baz = %d\n", total_biz_baz);
    write(1, output, strlen(output));

    snprintf(output, sizeof(output), "Total baz = %d\n", total_baz);
    write(1, output, strlen(output));

    snprintf(output, sizeof(output), "Total biz = %d\n", total_biz);
    write(1, output, strlen(output));

    return 0;

}