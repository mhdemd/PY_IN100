# Initialize an empty shopping cart dictionary
shopping_cart = {}

# Simulate an online store with available products and their prices
store_products = {
    'laptop': 1000,
    'smartphone': 500,
    'headphones': 100,
    'keyboard': 50
}

while True:
    print("\n====================")
    print("Available Products:")
    for index, (product, price) in enumerate(store_products.items(), 1):
        print(f"{index}. {product.capitalize()}: ${price}")

    print("====================")
    print("Shopping Cart:")
    if not shopping_cart:
        print("Your shopping cart is empty.")
    else:
        for cart_index, (item, quantity) in enumerate(shopping_cart.items(), 1):
            print(f"{cart_index}. {item.capitalize()}: {quantity}")

    print("====================")
    print("Options:")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Remove item from cart")
    print("4. Exit")
    print("====================")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        option_number = int(input("Enter the number of the product you want to add to your cart: "))
        if 1 <= option_number <= len(store_products):
            selected_product = list(store_products.keys())[option_number - 1]
            quantity_to_add = int(input(f"Enter the quantity of {selected_product.capitalize()} to add to your cart: "))
            current_quantity = shopping_cart.get(selected_product, 0)
            shopping_cart[selected_product] = current_quantity + quantity_to_add
            print(f"{quantity_to_add} {selected_product.capitalize()}(s) added to your cart.")
        else:
            print("Invalid option. Please choose a valid option.")
    elif choice == '2':
        print("Viewing Shopping Cart...")
    elif choice == '3':
        if not shopping_cart:
            print("Your shopping cart is empty. Nothing to remove.")
        else:
            option_number = int(input("Enter the number of the product you want to remove from your cart: "))
            if 1 <= option_number <= len(shopping_cart):
                selected_product = list(shopping_cart.keys())[option_number - 1]
                quantity_to_remove = int(input(f"Enter the quantity of {selected_product.capitalize()} to remove from your cart: "))
                current_quantity = shopping_cart[selected_product]
                if quantity_to_remove >= current_quantity:
                    del shopping_cart[selected_product]
                else:
                    shopping_cart[selected_product] = current_quantity - quantity_to_remove
                print(f"{quantity_to_remove} {selected_product.capitalize()}(s) removed from your cart.")
            else:
                print("Invalid option. Please choose a valid option.")
    elif choice == '4':
        print("Exiting. Thank you for shopping!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
