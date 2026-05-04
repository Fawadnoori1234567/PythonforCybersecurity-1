# IT102: Simple Input/Output Script

# 1. Ask the user the question and store the response
answer = input("Is today a good day? (y/n): ")

# 2. Check the input (using .lower() helps if they type 'Y')
if answer.lower() == "y":
       print("Yes it is")