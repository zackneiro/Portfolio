#!/bin/bash

# Compile the C program
gcc -Wall -o write write_int.c

# Check if compilation was successful
if [ $? -eq 0 ]; then
    echo "Compilation successful. Executable created: write"
else
    echo "Compilation failed."
fi