#!/usr/bin/env python3
# Script to collect user info and save to a file
# For educational purposes: Never provide real security answers!

def main():
    # Collect information from the user
    name = input("What is your name? ")
    color = input("What is your favorite color? ")
    pet = input("What was your first pet's name? ")
    maiden_name = input("What is your mother's maiden name? ")
    school = input("What elementary school did you attend? ")

    # Define the filename
    filename = "hackme.txt"

    # Open the file in write mode ('w')
    # This will create the file if it doesn't exist
    with open(filename, "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Favorite Color: {color}\n")
        f.write(f"First Pet: {pet}\n")
        f.write(f"Mother's Maiden Name: {maiden_name}\n")
        f.write(f"Elementary School: {school}\n")

    print(f"\nInformation successfully saved to {filename}")

if __name__ == "__main__":
    main()