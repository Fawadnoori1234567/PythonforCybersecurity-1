import base64

def main():
    # 1. Prompt for plaintext message
    user_input = input("Enter a message: ")

    # 2. Encode to Base64 (Convert string to bytes first)
    input_bytes = user_input.encode('utf-8')
    base64_bytes = base64.b64encode(input_bytes)
    encoded_message = base64_bytes.decode('utf-8')

    # 3. Decode back to plaintext
    decoded_bytes = base64.b64decode(base64_bytes)
    decoded_message = decoded_bytes.decode('utf-8')

    # 4. Confirm it matches
    match_confirmation = str(user_input == decoded_message)

    # Display Output
    print(f"Base64 encoded : {encoded_message}")
    print(f"Decoded message: {decoded_message}")
    print(f"Confirmation   : {match_confirmation}")

if __name__ == "__main__":
    main()