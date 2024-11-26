class Customer:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    def login(self, username, password):
        if self.username == username and self._password == password:
            return True
        else:
            return False
        
class VIPCustomer(Customer):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.membership_level = "Gold"

def register_customer(customers):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    customer_type = input("Enter your customer type (Regular|VIP): ").lower()

    if customer_type == "vip":
        customers[username] = VIPCustomer(username, password)
    else:
        customers[username] = Customer(username, password)
    
    print("Registration successful! welcome to our system.")

def main():
    customers = {}  # Database

    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username_input = input("Enter your username: ")
            password_input = input("Enter your password: ")

            if username_input in customers:
                if customers[username_input].login(username_input, password_input):
                    print("Login successfull!")
                    if isinstance(customers[username_input], VIPCustomer):
                        print("You are a VIP Customer!")
                    else:
                        print("You are a Regular Customer!")
                else:
                    print("Invalid username or password!")
            else:
                print("Invalid username or password!")

        elif choice == "2":
            register_customer(customers)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. please try again!")

main()
