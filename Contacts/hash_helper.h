#ifndef HASH_HELPER_H
#define HASH_HELPER_H

#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define TABLE_SIZE 26

typedef struct list // DEFINE NODE STRUCTURE
{
    char *name;
    struct list *next;
} node;

// FUNCTIONS PROTOTYPE
void add_person(node **contacts); // Append a new person to the hash table
int get_number_menu(const char *prompt); // Retrieve a user choice from the main menu
int get_choice_menu_print_contacts(void); // Retrieve user choice for the contact print menu
void get_name(const char *prompt, char **name); // Retrieve and validate a name from user input
void get_letter(char **letter); // Get a single alphabetical character for filtering contacts
size_t hash_name_function(const char *name); // Calculate hash index for a given name
void delete_person(node **contacts); // Remove a specified person from the hash table
void delete_all_contacts(node **contacts); // Delete all contacts from the hash table
void find_person(node **contacts, const char *prompt); // Locate a person in the hash table
void print_contacts(node **contacts); // Print contacts based on user-selected filter
void print_all_contacts(node **contacts); // Print all contacts in the hash table
void print_specific_contacts(node **contacts); // Print contacts starting with a specific letter

#endif // HASH_HELPER_H
