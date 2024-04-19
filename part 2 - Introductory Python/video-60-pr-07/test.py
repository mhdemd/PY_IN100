# Initialize an empty shopping cart dictionary
shopping_cart = {} # False

# Simulate an online store with available products and their prices
store_products = {
    'laptop' : 1000,
    'smartphone' : 500,
    'headphones' : 100,
    'keyboard' : 50,
}

# index = 1
# for product, price in store_products.items():
#     print(f"{index}. {product.capitalize()}: ${price}")
#     index += 1 # index = index + 1

# for index, (product, price) in enumerate(store_products.items(), 22):
#     print(f"{index}. {product.capitalize()}: ${price}")

while True:
    print("\n==================")
    print("Available Products:")
    for index, (product, price) in enumerate(store_products.items(), 1):
        print(f"{index}. {product.capitalize()}: ${price}")

    print("==================")
    print("Shopping Cart:")
    if not shopping_cart:
        print("Your shopping cart is empty.")
    else:
        for cart_index, (item, quantity) in enumerate(shopping_cart.items(), 1):
            print(f"{cart_index}. {item.capitalize()}: {quantity}")
    
    print("==================")
    print("Options:")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Remove item from cart")
    print("4. Exit")
    print("==================")
    
    choice = input("Enter your choice (1-4): \n")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
