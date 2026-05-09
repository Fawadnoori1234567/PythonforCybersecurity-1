#!/usr/bin/env python3
# Caesar Cipher Lab IT102
# Objective: Encrypt and Decrypt messages using a variable shift

def caesar_cipher():
    # 1. Prompts the user to input a message
    message = input("Enter a message: ")
    
    # 2. Asks for a shift value (integer) between 1 and 25
    try:
        shift = int(input("Enter the shift value (1-25): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # 3. Encrypt the message
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Calculate the ASCII offset (65 for Upper, 97 for Lower)
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap using modulo 26
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_message += new_char
        else:
            # Keep spaces and punctuation as they are
            encrypted_message += char

    # 4. Displays the encrypted message
    print(f"Encrypted message: {encrypted_message}")

    # 5. Includes a decryption option
    decrypt_choice = input("Decrypt the message? (yes/no): ").lower()
    
    if decrypt_choice == "yes":
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                # Reverse the shift
                new_char = chr(start + (ord(char) - start - shift) % 26)
                decrypted_message += new_char
            else:
                decrypted_message += char
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    caesar_cipher()
    