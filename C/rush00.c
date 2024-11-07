#include <unistd.h>

void rush00(int x, int y)
{   
     x = 123; // test variables 
     y = 200; 
    int width = y - 2; // amount of characters to print between 'o' in y cordinates
    int sticks = x - 2; // amount of sticks to print in x cordinates

    // First case: when we have only width 
    if (x > 1 && y == 1 && x < 200)
    {   
        write(1, "o", 1); // printing corner char '0'
        for (int i = 0; i < sticks ; i++) // for-loop to print width 
        {
            write(1, "-", 1); // printing the '-' char
        }
        write(1, "o\n", 2); //printing the last corner character followed by the newline
    }

    // Case 2: if we have width and length arguments
    else if (x > 1 && y > 1 && x < 200 && y < 200)
    {   
        // this part prints the top border
        write(1, "o", 1);
        for (int i = 0; i < sticks ; i++)
        {
            write(1, "-", 1);
        }
        write(1, "o\n", 2);

        // this part prints the left and right borders
        for (int f = 0; f < width; f++)
            {
                write(1, "|", 1);
                for (int k = 0; k < sticks; k++)
                {
                    write(1, " ", 1);
                }
                write(1, "|", 1);
                write(1, "\n", 1);
            }
            write(1, "o", 1);
            // this part prints the bottom border
            for (int i = 0; i < sticks ; i++)
            {
                write(1, "-", 1);
            }
            write(1, "o\n", 2);
    }
    // Case 3: if we have only length 
    else if (x == 1 && y > 1 && y < 200)
    {   
        // This block will only print the left border
        write(1, "o\n", 2);
        for (int g = 0; g < width; g++)
        {
            write(1, "|\n", 2);
        }
        write(1, "o\n", 2);
    }

    // Case 4: if width and length = 1, just print the 'o'
    else if (x == 1 && y == 1)
    {
        write(1, "o\n", 2);
    }
    else // Case 5: print the error message since the arguments are less than 1 or greater than 200
    {
        write(1, "_arguments_value_error_\n", 24);
    }
}