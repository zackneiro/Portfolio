#include "hash_helper.h"


int get_number_menu(const char *text) // function to get number
{
    int number, result;
    printf("%s\n", text);
    do
    {
        result = scanf("%d", &number); // read the input from user

        if (result == 1 && number <= 6 && number > 0)
        {
            // If a valid integer is entered, break out of the loop.
            break;
        }
        else
        {
            // Clear the input buffer if the input was not a valid integer.
            while (getchar() != '\n')
                ;
            printf("Invalid input. Please enter a valid integer: ");
        }
    }
    while (1);
    return number;
}

int get_choice_menu_print_contacts(void) // function to get number
{
    int number, result;
    do
    {
        result = scanf("%d", &number); // read the input from user

        if (result == 1 && number <= 3 && number > 0)
        {
            // If a valid integer is entered, break out of the loop.
            break;
        }
        else
        {
            // Clear the input buffer if the input was not a valid integer.
            while (getchar() != '\n')
                ;
            printf("Invalid choice. Please enter a valid choice: ");
        }
    }
    while (1);
    return number;
}

void get_name(const char *text, char **name) // function to get valid name
{
    char buffer[100]; // Temporary buffer to store the name
    printf("%s\n", text); // Prompt the user for input

    // This loop discards any characters remaining in the standard input buffer up to a newline or EOF.
    // It's used to clean up the buffer before reading the next input.
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { /* discard characters */ }

    if (fgets(buffer, sizeof(buffer), stdin)) // Attempt to read a line of text from stdin
    {
        buffer[strcspn(buffer, "\n")] = 0; // Remove any newline character from the end of the string
        *name = strdup(buffer); // Duplicate the string read into buffer to dynamically allocate memory for name
        if (*name == NULL) // Check if memory allocation failed
        {
            fprintf(stderr, "Failed to allocate memory for name.\n"); // Output error message to stderr
            exit(EXIT_FAILURE); // Exit the program indicating a failure, typically defined as 1
        }
    }
    else // if fgets fails to read a line...
    {
        if (feof(stdin)) // Check if end of file (EOF) has been reached on stdin
        {
            fprintf(stderr, "End of file reached.\n"); // Inform user EOF was reached
            exit(EXIT_FAILURE); // Exit the program with a failure status
        }
        else if (ferror(stdin)) // Check if a read error occurred on stdin
        {
            perror("Error reading from stdin"); // Print the system error message related to the read error
            exit(EXIT_FAILURE); // Exit the program indicating a failure
        }
        fprintf(stderr, "Failed to read name.\n"); // General error message if fgets failed for reasons other than EOF or read error
        exit(EXIT_FAILURE); // Exit the program with a failure status
    }
}

void get_letter(char **letter)
{
    char buffer[2]; // Temporary buffer to store the name

    // This loop discards any characters remaining in the standard input buffer up to a newline or EOF.
    // It's used to clean up the buffer before reading the next input.
    int c;
    while ((c = getchar()) != '\n' && c != EOF) { /* discard characters */ }

    if (fgets(buffer, sizeof(buffer), stdin)) // Attempt to read a line of text from stdin
    {
        buffer[strcspn(buffer, "\n")] = 0; // Remove any newline character from the end of the string
        *letter = strdup(buffer); // Duplicate the string read into buffer to dynamically allocate memory for name
        if (*letter == NULL) // Check if memory allocation failed
        {
            fprintf(stderr, "Failed to allocate memory for letter.\n"); // Output error message to stderr
            exit(EXIT_FAILURE); // Exit the program indicating a failure, typically defined as 1
        }
    }
    else // if fgets fails to read a line...
    {
        if (feof(stdin)) // Check if end of file (EOF) has been reached on stdin
        {
            fprintf(stderr, "End of file reached.\n"); // Inform user EOF was reached
            exit(EXIT_FAILURE); // Exit the program with a failure status
        }
        else if (ferror(stdin)) // Check if a read error occurred on stdin
        {
            perror("Error reading from stdin"); // Print the system error message related to the read error
            exit(EXIT_FAILURE); // Exit the program indicating a failure
        }
        fprintf(stderr, "Failed to read letter.\n"); // General error message if fgets failed for reasons other than EOF or read error
        exit(EXIT_FAILURE); // Exit the program with a failure status
    }
}



size_t hash_name_function(const char *name) // hash function
{
    // Base case: If the name is NULL or empty, return an invalid index
    if (name == NULL || *name == '\0') {
        return -1;  // Assuming unsigned, this will wrap around to the maximum value
    }

    // Convert the first character to uppercase to ignore case differences
    char firstChar = toupper(name[0]);

    // Ensure it's a valid letter
    if (firstChar < 'A' || firstChar > 'Z') {
        return -1;
    }

    // Map 'A' to 0, 'B' to 1, ..., 'Z' to 25
    return (firstChar - 'A') % TABLE_SIZE;
}

void find_person(node **contacts, const char *promt) // function to find name in list and print info if found
{
    size_t key = 0;
    char *name = NULL;
    printf("%s", promt); // print start text of searching for user

    get_name("Please give us a name you are looking for:", &name); // get name user looks for
    key  = hash_name_function(name); // get key to acsess right list

     bool found = false; // set bool value to false as a default

    for (node *ptr = contacts[key]; ptr != NULL; ptr = ptr->next) // iterate a loop through list accesed with key
    {
        if (strcmp(ptr->name, name) == 0) // check if name in the current node is that we are looking for
        {
            found = true; // set a value to true if found
            break; // stop for-loop and exit
        }
    }

    if (found) // if contact is found, then print the message to user that person in his contacts
    {
        printf("%s is in your contacts.\n", name);
        free(name);
    }
    else // if not program tells about that
    {
        printf("%s is not in your contacts.\n", name);
        free(name);
    }


}

void add_person(node **contacts) // append node function
{
    size_t key = 0;
    char *name = NULL;


    get_name("Please give us a name you want to add in your contacts: ", &name); // get name and key we work with
    key = hash_name_function(name);

    node *new_node = malloc(sizeof(node)); // allocate memory for new node

    if (new_node == NULL) // if NULL - exit.
    {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(1);
    }

    new_node->name = name; // updating value with name from user
    new_node->next = contacts[key]; // point new node to the current head of the list
    contacts[key] = new_node; // point to new node

}

void delete_person(node **contacts) //function to delete person from list
{
    size_t key = 0;
    char *name = NULL;

    get_name("Please enter the name you are looking for: ", &name); // get name we are gonna work with and removes the first occurrence of a contact with the given name

    if (name == NULL) // if memory allocation for name is failed send a message to stderr and go back to menu
    {
        fprintf(stderr, "Failed to get name.\n");
        return;
    }
    key = hash_name_function(name); // get the key and determines which bucket in the hash table to search, based on the name

    if (contacts[key] == NULL) // if list is empty stop
    {
        printf("No contact found under this name.\n"); // print message
        free(name); // free name to prevent memory leaks
        return; // go back to menu
    }

    node *current = contacts[key]; // current position in the list at contacts[i]
    node *previous = NULL; // set as "NULL" because it tracks the node before current in the list, and there is no node before the first
    while (current != NULL) // iterate while-loop over list
    {
        if (strcmp(current->name, name) == 0) // "strcmp" returns 0 if the strings are identical, which is why the condition checks for equality
                                              // function ensures the list remains linked after a node is removed.
        {
            if (previous == NULL) // if previous is NULL
            {
                contacts[key] = current->next; // move head pointer to the next node
            }
            else
            {
                previous->next = current->next; // move previous to next node
            }
            free(current); // free current node
            printf("Contact was sucsessfully deleted!\n"); // print message about sucsessful deletion
            return; // go back to menu
        }
        previous = current; // prepares for the next iteration by moving both pointers forward in the list.
        current = current->next;
    }
    printf("Number %s not found in the list.\n", name); // print message about sucessful deletion
    free(name); // free name to prevent memory leaks
}
void delete_all_contacts(node **contacts) // function to print all the names in list
{

    for (int i = 0; i < 26; i++) // Adjust loop to correctly iterate over array bounds
    {
        node *ptr = contacts[i]; // current position in the list at contacts[i]
        while (ptr != NULL)
        {
            node *tmp = ptr->next; // save the next node
            free(ptr); // free the current node
            ptr = tmp; // move to the next node
        }
        contacts[i] = NULL; // after freeing all nodes, set the head of the list to NULL
    }
}
void print_contacts(node **conctacts) // function to print user's contacts
{
    int choice = 0; // initialize integer choice
    do
    {
        printf("\nDo you want to see all your contacnts or some specific?\n" // Ask user for a choice to understand next move
            "1 - All.\n" // if choosen print all user's contacts in alphabetical way
            "2 - Specific.\n" // if chosen print some contacts depending on user's wish
            "3 - Go back to menu\n"); // return user's back to menu

       choice = get_choice_menu_print_contacts(); // function to get correct choice from user

       switch(choice) // procceed to next step depending on user's choice and using switch - statment
       {
            case 1:
                print_all_contacts(conctacts);
                break;
            case 2:
                print_specific_contacts(conctacts);
                break;
            case 3:
                break;
            default:
                printf("Invalid option, please choose a valid number (1-3).\n");
                break;
       }
    }
    while (choice != 3);
}

void print_all_contacts(node **contacts) // function to print all user's contact in aplhabetical way
{
    // iterate a for-loop to go through all the lists
    printf("Here are all your contacts: \n");
    for (int i = 0; i < 26; i++)
    {
        node *ptr = contacts[i];
        if (ptr == NULL) continue; // if no contacts in the list, stop and go to next list
        while (ptr != NULL) // iterate while-loop over list till "NULL" is met
        {
            printf("%s\n", ptr->name); // print the name
            ptr = ptr->next; // move to the next node
        }
    }
    printf("\n");
}

void print_specific_contacts(node **contacts)
{
    // Request a letter from the user to filter contacts by the initial character
    char *letter = NULL;
    size_t key = 0;
    printf("Please enter firs letter of names you want to see: ");
    get_letter(&letter); // // Get a single initial letter for name filtering
    key = hash_name_function(letter); // Calculate hash index based on the initial letter to directly access relevant list
    node *current  = contacts[key]; // Start from the first contact in the designated hash bucket

    if (contacts[key] == NULL) // Inform the user if no contacts start with the chosen letter
    {
        printf("You don't have contacts who starts with this letter.\n");
        return;
    }

    printf("Here are your contacts who starts with letter %s: \n", letter); // Display all contacts starting with the specified letter

    while (current != NULL)
    {
        printf("%s\n", current->name);
        current = current->next;
    }

    printf("\n");
    free(letter); // Clean up the memory allocated for the letter
}
