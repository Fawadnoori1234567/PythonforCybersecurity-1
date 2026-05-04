# Ask the user for input
user_input = input("Is today a good day? (y/n) ")

# Check if the input is 'y'
if user_input.lower() == 'y':
    # Use a loop to print the message 10 times
    for i in range(10):
        print("Yeah it is")