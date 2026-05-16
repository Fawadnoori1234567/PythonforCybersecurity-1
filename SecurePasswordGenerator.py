#!/usr/bin/env python3
"""
IT102: Secure Password Generator Assignment
Description: Generates secure, random passwords based on user-defined criteria.
Practices: String manipulation, randomization, and user input handling.
"""

import random
import string
import sys

def get_password_criteria():
    print("\n--- Password Criteria Setup ---")
    
    # 1. Force a minimum length of 8 characters
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            if length >= 8:
                break
            print("Security Warning: Passwords must be at least 8 characters long.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    # 2. Gather character set preferences
    print("\nSelect character types to include (Y/N):")
    include_upper = input("Include Uppercase letters (A-Z)? ").strip().upper() == 'Y'
    include_lower = input("Include Lowercase letters (a-z)? ").strip().upper() == 'Y'
    include_digits = input("Include Numbers (0-9)? ").strip().upper() == 'Y'
    include_special = input("Include Special Characters (!@#$...)? ").strip().upper() == 'Y'
    
    # Validation: Ensure at least one category is selected
    if not (include_upper or include_lower or include_digits or include_special):
        print("\n[!] Error: You must select at least one character category!")
        return get_password_criteria() # Restart criteria gathering
        
    return length, include_upper, include_lower, include_digits, include_special


def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Resource pools
    upper_pool = string.ascii_uppercase
    lower_pool = string.ascii_lowercase
    digit_pool = string.digits
    special_pool = string.punctuation # Contains !@#$%^&*()_+-=[]{}|;:'",.<>/?/
    
    password_pool = ""
    guaranteed_characters = []
    
    # Guarantee at least one character from each selected category
    if use_upper:
        password_pool += upper_pool
        guaranteed_characters.append(random.choice(upper_pool))
    if use_lower:
        password_pool += lower_pool
        guaranteed_characters.append(random.choice(lower_pool))
    if use_digits:
        password_pool += digit_pool
        guaranteed_characters.append(random.choice(digit_pool))
    if use_special:
        password_pool += special_pool
        guaranteed_characters.append(random.choice(special_pool))
        
    # Fill the remaining length with random choices from the combined pool
    remaining_length = length - len(guaranteed_characters)
    for _ in range(remaining_length):
        guaranteed_characters.append(random.choice(password_pool))
        
    # Shuffle the resulting list so the guaranteed characters aren't predictable
    random.shuffle(guaranteed_characters)
    
    # Turn list back into a single string
    return "".join(guaranteed_characters)


def main():
    print("=========================================")
    print("      SECURE PASSWORD GENERATOR Tool     ")
    print("=========================================")
    
    while True:
        # Get criteria
        length, use_upper, use_lower, use_digits, use_special = get_password_criteria()
        
        # Generate and show password
        secure_password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print("\n-----------------------------------------")
        print(f"Generated Secure Password: {secure_password}")
        print("-----------------------------------------")
        
        # Ask to repeat or exit
        choice = input("\nWould you like to generate another password? (Y/N): ").strip().upper()
        if choice != 'Y':
            print("\nExiting Secure Password Generator. Stay safe online!")
            break

if __name__ == "__main__":
    main()