# Collect information from the user
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
maiden_name = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

# Save the information to a file
with open("hackme.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorite Color: {color}\n")
    file.write(f"First Pet's Name: {pet}\n")
    file.write(f"Mother's Maiden Name: {maiden_name}\n")
    file.write(f"Elementary School: {school}\n")

print("Information has been saved to hackme.txt")
