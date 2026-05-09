# 1. Create the function
def send_message():
    # Move the loop inside this function
    for i in range(5):
        print("Yeah it is")

# 2. Update the conditional statement
# This checks if a condition is met before calling the function
status = "active" # You can change this variable to test the logic

if status == "active":
    send_message() # This calls the function you created above
else:
    print("Condition not met.")
    