"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####
def add_to_basket(item: dict) -> list:
    '''Adds item to basket'''
    basket.append(item)
    return basket


def generate_receipt(final_basket: list) -> str:
    '''Returns the generated receipt'''
    if len(final_basket) == 0:
        return "Basket is empty"

    total = 0
    shopping_list = []
    counted_shopping_list = {}

    for existing_item in final_basket:
        name = existing_item["name"]
        price = existing_item["price"]
        key = name, price
        counted_shopping_list[key] = counted_shopping_list.get((name, price),0) + 1

    for (key), count in counted_shopping_list.items():
        duplicates = price * count
        total += duplicates

        if price == 0:
            shopping_list.append(f"{name} x {count} - Free")
        else:
            shopping_list.append(f"{name} x {count} - £{total:.2f}")

    shopping_list.append(f"Total: £{total:.2f}")
    receipt = "\n".join(shopping_list)

    return receipt

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
