from json import dumps

import prices


api = prices.YGOPricesAPI()

done = False

while not done:
    
    choice = input("name or tag: ")
    prices = {}

    if "n" in choice:
        name = input("Enter a card name: ")
        prices = api.get_price_by_name(name)
    elif "t" in choice:
        name = input("Enter a tag: ")
        prices = api.get_price_by_name(name)

    if prices:
        print(dumps(prices, indent=2))
