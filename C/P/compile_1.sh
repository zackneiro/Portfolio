#!/bin/bash

# Compile the C program
gcc -Wall main.c -o even

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Executable created: write"
else
    echo "Compilation failed."
fi