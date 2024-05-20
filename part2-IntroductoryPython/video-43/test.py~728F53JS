# Define an initial dictionary
dict = {
    'name': 'John',
    'age': '25',
    'city': 'New York'
}

# Display the initial dictionary
print("Initial Dict:\n", dict)

# Get input from the user for a key
user_input = input("Enter a key to check: ")

# Check if the key exists using the 'in' keyword
if user_input in dict:
    print(f"Key '{user_input}' exist. value: {dict[user_input]}")

    # Ask the user to remove (1) or modify (2) the key-value pair
    chioce = input("Do you want to:\n 1-remove \n 2-modify \n Enter 1 or 2:")

    if chioce == "1":
        # Use 'pop' to remove the key-value
        removed_item = dict.pop(user_input)
        print(f"Removed '{user_input}: {removed_item}'")
    elif chioce == "2":
        # Get input for the new value to update the key
        new_value = input(f"Enter new value for '{user_input}': ")

        # Use 'update' or ...
        dict[user_input] = new_value
        print(f"Update '{user_input}' to : {new_value}")
        print(dict)
    else:
        print("Invalid chioce!")





else:
    print(f"Key '{user_input}' does not exist.")