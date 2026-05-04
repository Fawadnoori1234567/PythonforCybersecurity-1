#!/usr/bin/env python3
# Script to read target information from a file

# Define the filename
filename = "hackme.txt"

try:
    # Use the 'with' statement to open and automatically close the file
    with open(filename, "r") as target_file:
        
        # Read the entire content of the file
        content = target_file.read()
        
        # Print the header message
        print("Here is someone to hack - information")
        print("-" * 40) # Adds a visual separator line
        
        # Print the data found in the file
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found in this directory.")