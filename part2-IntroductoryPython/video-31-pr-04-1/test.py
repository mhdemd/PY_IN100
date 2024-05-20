# Initialize empty person information list
person_info = ["", "", 0]

# Get person information
person_info[0] = input("Enter your first name: ")
person_info[1] = input("Enter your last name: ")

# Get a valid age
age_input = input("Enter your age: ")

if age_input.isdigit():
    person_info[2] = int(age_input)
else:
    print("Invalid age. Please enter a valid age (numeric).")
    exit()

# Print initial person information
print("Congratulations!")
print("You have successfully entered the following information:")
print("First Name: " + person_info[0])
print("Last Name: " + person_info[1])
print("Age: " + str(person_info[2]))

# Menu for updating information
print("\nOptions for modification:")
print("1. Update first name")
print("2. Update last name")
print("3. Update age")

# Get a valid option
option_input = input("Enter your choice (1, 2, or 3): ")
if option_input.isdigit() and int(option_input) in [1, 2, 3]:
    option = int(option_input)
else:
    print("Invalid option. Please enter a number between 1 and 3.")

# Update information based on the selected option
if option == 1:
    person_info[0] = input("Enter the new first name: ")
elif option == 2:
    person_info[1] = input("Enter the new last name: ")
elif option == 3:
    # Get a valid new age
    new_age_input = input("Enter the new age: ")
    if new_age_input.isdigit():
        person_info[2] = int(new_age_input)
    else:
        print("Invalid age. Please enter a valid age (numeric).")

# Print updated person information
print("\nUpdated information:")
print("First Name: " + person_info[0])
print("Last Name: " + person_info[1])
print("Age: " + str(person_info[2]))
