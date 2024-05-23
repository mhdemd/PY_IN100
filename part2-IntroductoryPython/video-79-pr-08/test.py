# Initialize an empty shopping cart dictionary
shopping_cart = {}

# Simulate an online store with available products and their prices
store_products = {
    'laptop': 1000,
    'smartphone': 500,  # 2
    'headphones': 100,
    'keyboard': 50,
}

def display_products(store_products):
    print("\n==================")
    print("Available Products:")
    for index, (product, price) in enumerate(store_products.items(), 1):
        print(f"{index}. {product.capitalize()}: ${price}")
    print("==================")

def display_cart(shopping_cart):
    print("Shopping Cart:")
    if not shopping_cart:
        print("Your shopping cart is empty.")
    else:
        for cartIndex, (item, quantity) in enumerate(shopping_cart.items(), 1):
            print(f"{cartIndex}. {item.capitalize()}: {quantity}")
    print("==================")

def add_to_cart(store_products, shopping_cart):
    option_number = int(input("Enter the number of the product"
                                "you want to add to your cart: \n"))
    if 1 <= option_number <= len(store_products):
        list_keys_store_product = list(store_products.keys())
        selected_product = list_keys_store_product[option_number - 1]
        quantity_to_add = int(input(f"Enter the quantity of"
                                        f"{selected_product.capitalize()}"
                                            "to add to your cart: \n"))
        current_quantity = shopping_cart.get(selected_product, 0)
        new_quantity = quantity_to_add + current_quantity
        shopping_cart[selected_product] = new_quantity
        print(f"{quantity_to_add} {selected_product.capitalize()}(s)\
                added to your cart.")
    else:
        print("Invalid option. Please choose a valid option.")

def remove_from_cart(shopping_cart):
    if not shopping_cart:
        print("Your shopping cart is empty. Nothing to remove!")
    else:
        option_number = int(input("Enter the number of the"
                                    "product you want to remove"
                                    "from your cart: \n"))
        if 1 <= option_number <= len(shopping_cart):
            list_keys_shopping_cart = list(shopping_cart.keys())
            selected_product = list_keys_shopping_cart[option_number - 1]
            quantity_to_remove = int(input(f"Enter the quantity of"
                                    f"{selected_product.capitalize()}"
                                    "to remove from your cart: \n"))
            current_quantity = shopping_cart[selected_product]
            if quantity_to_remove >= current_quantity:
                del shopping_cart[selected_product]  # 6 > 5
            else:  # 2 < 5
                update_quantity = current_quantity - quantity_to_remove
                shopping_cart[selected_product] = update_quantity
        else:
            print("Invalid option. Please choose a valid option!")

def main():
    while True:
        display_products(store_products)
        display_cart(shopping_cart)

        print("Options:")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Exit")
        print("==================")

        choice = input("Enter your choice (1-4): \n")

        if choice == "1":
            add_to_cart(store_products, shopping_cart)
        elif choice == "2":
            display_cart(shopping_cart)
        elif choice == "3":
            remove_from_cart(shopping_cart)
        elif choice == "4":
            print("Exiting. Tank you for shopping!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main loop
main()
