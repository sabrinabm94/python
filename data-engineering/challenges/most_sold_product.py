import sys


def most_sold_product(products):
    count = {}

    # Count occurrences of each product
    for product in products:
        if product in count:
            count[product] += 1
        else:
            count[product] = 1

    max_product = None
    max_count = 0

    # Find the product with the highest count
    for product, quantity in count.items():
        if quantity > max_count:
            max_count = quantity
            max_product = product

    return max_product


def get_product_input():
    # Get user input in a single line
    # entry = str(sys.stdin.readline()).strip()
    entry = "apple, banana, apple, orange, banana, apple"

    products = [
        product.strip() for product in entry.split(",")
    ]  # Removes extra spaces around each product

    return products


# Get the list of products and find the most sold product
products = get_product_input()
print(most_sold_product(products))
