"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []

def add_to_basket(item: dict) -> list:
    '''Adds items to a basket dictionary.'''
    basket.append(item)
    return basket


def generate_receipt(final_basket: list) -> str:
    '''Returns the generated receipt'''

    #Checks if basket is empty and returns "Basket is empty if it is."
    if len(final_basket) == 0:
        return "Basket is empty"

    total = 0
    shopping_list = []

    for item in final_basket:
        name = item["name"]
        price = item["price"]
        if price == 0:
            shopping_list.append(f"{name} - Free")
        else:
            shopping_list.append(f"{name} - £{price:.2f}")
        total += price

    #Totals all items in our shopping_list
    shopping_list.append(f"Total: £{total:.2f}")
    receipt = "\n".join(shopping_list)

    return receipt


if __name__ == "__main__":
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
