# Initialize an empty shopping cart dictionary
shopping_cart = {}

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
    print("/n==================")
    print("Available Products:")
    for index, (product, price) in enumerate(store_products.items(), 1):
        print(f"{index}. {product.capitalize()}: ${price}")

    break
