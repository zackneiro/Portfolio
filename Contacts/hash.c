#include "hash_helper.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

node *contacts[25] = {NULL};

int main(void)
{
    int choice = 0;
    do
    {
        printf("\nMenu:\n"
               "1 - Add new contact.\n"
               "2 - Find a person.\n"
               "3 - Delete a person.\n"
               "4 - Delete all contacts.\n"
               "5 - Print contacts.\n"
               "6 - Exit.\n");
        choice = get_number_menu("Choose your option: ");

        if (choice < 0 || choice > 6)
        {
            continue;
        }

        switch(choice)
        {
            case 1:
                add_person(contacts);
                break;
            case 2:
                find_person(contacts, "Search...\n");
                break;
            case 3:
                delete_person(contacts);
                break;
            case 4:
                delete_all_contacts(contacts);
                break;
            case 5:
                print_contacts(contacts);
                break;
            case 6:
                printf("Exiting the program...\n");
                delete_all_contacts(contacts);
                break;
            default:
                printf("Invalid option, please choose a valid number (1-6).\n");
                break;
        }

    }
    while(choice != 6);
    return 0;
}