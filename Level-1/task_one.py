"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

final_basket = []

def add_to_basket(item: dict) -> list:
    '''Adds items to a basket dictionary.'''
    final_basket.append(item)
    return final_basket


def generate_receipt(basket: list) -> str:
    '''Returns the generated receipt'''

    #Checks if basket is empty and returns "Basket is empty if it is."
    if len(basket) == 0:
        return "Basket is empty"

    '''Create a total we can add to, as well as
    a list we can print the items we want to append'''
    total = 0
    shopping_list = []

    '''Iterates through our dictionary and stores names 
    and prices into new variables'''
    for item in basket:
        name = item["name"]
        price = item["price"]
        '''If the price of an item is 0, we add the items name 
        followed by "- free" to our empty shopping_list'''
        if price == 0:
            shopping_list.append(f"{name} - Free")
        #Otherwise we append the item to our shopping list
        else:
            shopping_list.append(f"{name} - £{price:.2f}")
        total += price

    #Totals all items in our shopping_list
    shopping_list.append(f"Total: £{total:.2f}")
    '''.join() method is used to convert our list into a str 
    and print every element on a new line'''
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
    print(generate_receipt(final_basket))
