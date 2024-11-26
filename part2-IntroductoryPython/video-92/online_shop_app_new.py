import time

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def display_cart(self):
        print("Shopping Cart:")
        if not self.cart:
            print("Your shopping cart is empty.")
        else:
            for index, (item, quantity) in enumerate(self.cart.items(), 1):
                print(f"{index}. {item.capitalize()}: {quantity}")
        print("==================")

    def add_to_cart(self, product_name, product_price, quantity):
        current_quantity = self.cart.get(product_name, 0)
        new_quantity = quantity + current_quantity
        self.cart[product_name] = {'price': product_price, 'quantity': new_quantity}
        print(f"{quantity} {product_name.capitalize()}(s) added to your cart.")

    def remove_from_cart(self, option_number, quantity_to_remove):
        if 1 <= option_number <= len(self.cart):
            list_keys_cart = list(self.cart.keys())
            selected_product = list_keys_cart[option_number - 1]
            current_quantity = self.cart[selected_product]['quantity']
            if quantity_to_remove >= current_quantity:
                del self.cart[selected_product]
            else:
                self.cart[selected_product]['quantity'] = current_quantity - quantity_to_remove
        else:
            print("Invalid option. Please choose a valid option!")

class Store:
    def __init__(self, products):
        self.products = products

    def display_products(self):
        print("\n==================")
        print("Available Products:")
        for index, (name, price) in enumerate(self.products.items(), 1):
            print(f"{index}. {name.capitalize()}: ${price}")
        print("==================")

    def filter_above_400(self):
        return {name: price for name, price in self.products.items() if price > 400}

def log_add_to_cart(func):
    def wrapper(*args, **kwargs):
        print("Adding item to cart...")
        time.sleep(2)
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper

class OnlineStoreApp:
    def __init__(self, store, cart):
        self.store = store
        self.cart = cart

    @log_add_to_cart
    def add_to_cart(self, option_number, quantity):
        if 1 <= option_number <= len(self.store.products):
            selected_product_name = list(self.store.products.keys())[option_number - 1]
            selected_product_price = self.store.products[selected_product_name]
            self.cart.add_to_cart(selected_product_name, selected_product_price, quantity)
        else:
            print("Invalid option. Please choose a valid option.")

    def run(self):
        while True:
            self.store.display_products()
            self.cart.display_cart()

            print("Options:")
            print("1. Add item to cart")
            print("2. View cart")
            print("3. Remove item from cart")
            print("4. Filter above $400")
            print("5. Exit")
            print("==================")

            choice = input("Enter your choice (1-5): \n")

            if choice == "1":
                option_number = int(input("Enter the number of the product you want to add to your cart: \n"))
                quantity_to_add = int(input("Enter the quantity of product to add to your cart: \n"))
                self.add_to_cart(option_number, quantity_to_add)
            elif choice == "2":
                self.cart.display_cart()
            elif choice == "3":
                if not self.cart.cart:
                    print("Your shopping cart is empty. Nothing to remove!")
                else:
                    option_number = int(input("Enter the number of the product you want to remove from your cart: \n"))
                    quantity_to_remove = int(input("Enter the quantity of product to remove from your cart: \n"))
                    self.cart.remove_from_cart(option_number, quantity_to_remove)
            elif choice == "4":
                filtered_products = self.store.filter_above_400()
                print("Products above $400: ")
                for name, price in filtered_products.items():
                    print(f"{name.capitalize()}: ${price}")
            elif choice == "5":
                print("Exiting. Thank you for shopping!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

# Initialize store products
products = {
    'laptop': 1000,
    'smartphone': 500,
    'headphones': 100,
    'keyboard': 50
}

# Create store and shopping cart objects
store = Store(products)
cart = ShoppingCart()

# Run the main loop
app = OnlineStoreApp(store, cart)
app.run()
