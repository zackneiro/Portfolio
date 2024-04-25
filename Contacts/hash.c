#include "hash_helper.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

node *contacts[25] = {NULL}; // Array of pointers to 'node' structures, used as a hash table to organize contacts by a hash index.


int main(void)
{
    int choice = 0;
    // Continuously display the menu and process user input until the user chooses to exit.
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

        if (choice < 0 || choice > 6) // Ensure that the user's choice is within the valid range. Ignore out-of-range inputs.
        {
            continue;
        }

        switch(choice)
        {
            // Add a new contact to the hash table.
            case 1:
                add_person(contacts);
                break;
            // Search for a person in the hash table and display if found.
            case 2:
                find_person(contacts, "Search...\n");
                break;
            // Delete a specified contact from the hash table.
            case 3:
                delete_person(contacts);
                break;
            // Remove all contacts from the hash table.
            case 4:
                delete_all_contacts(contacts);
                break;
            // Display all contacts currently stored in the hash table.
            case 5:
                print_contacts(contacts);
                break;
            // Exit the program and clean up all contacts from memory.
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