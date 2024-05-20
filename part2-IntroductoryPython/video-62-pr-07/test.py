# Initialize an empty shopping cart dictionary
shopping_cart = {} # False

# Simulate an online store with available products and their prices
store_products = {
    'laptop' : 1000,
    'smartphone' : 500, # 2
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
        option_number = int(input("Enter the number of the product you want to add to your cart: \n"))
        if 1<= option_number <= len(store_products):
            list_keys_store_product = list(store_products.keys())
            selected_product = list_keys_store_product[option_number - 1] # 2 - 1
            # print(selected_product)
            quantity_to_add = int(input(f"Enter the quantity of {selected_product.capitalize()} to add to your cart: \n"))
            current_quantity = shopping_cart.get(selected_product, 0)
            shopping_cart[selected_product] = quantity_to_add + current_quantity
            print(f"{quantity_to_add} {selected_product.capitalize()}(s) added to your cart.")            
        else:
            print("Invalid option. Please choose a valid option.")
    elif choice == "2":
        print("Viewing Shopping Cart...")
    elif choice == "3":
        if not shopping_cart:
            print("Your shopping cart is empty. Nothing to remove!")
        else:
            option_number = int(input("Enter the number of the product you want to remove from your cart: \n"))
            if 1 <= option_number <= len(shopping_cart):
                list_keys_shopping_cart = list(shopping_cart.keys())
                selected_product = list_keys_shopping_cart[option_number - 1] # 2 - 1 !!
                quantity_to_remove = int(input(f"Enter the quantity of {selected_product.capitalize()} to remove from your cart: \n"))
                current_quantity = shopping_cart[selected_product]
                if quantity_to_remove >= current_quantity:
                    del shopping_cart[selected_product] # 6 > 5
                else: # 2 < 5
                    shopping_cart[selected_product] = current_quantity - quantity_to_remove
            else:
                print("Invalid option. Please choose a valid option!")
    elif choice == "4":
        print("Exiting. Tank you for shopping!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
