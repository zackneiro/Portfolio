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
void add_person(node **contacts); // funtcion to append node to list
int get_number_menu(const char *text); // function to get choice from user in the main menu
int get_choice_menu_print_contacts(void); // fuction to get choice from user in printing contacts part of code
void get_name(const char *text, char **name); // function to get valid name
void get_letter(char **letter); // fuction to get a valid letter for specific printing
size_t hash_name_function(const char *name); // hash function
void delete_person(node **contacts); //function to delete node from list
void delete_all_contacts(node **contacts); // function to print all the names in list
void find_person(node **contacts, const char *promt);
void print_contacts(node **contacts);
void print_all_contacts(node **contacts);
void print_specific_contacts(node **contacts);

#endif // HASH_HELPER_H
