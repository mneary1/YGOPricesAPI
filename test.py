from prices import YGOPriceAPI
from json import dumps 

api = YGOPriceAPI()

done = False

while not done:
    
    choice = raw_input("name or tag: ")
    prices = {}

    if "n" in choice:
        name = raw_input("Enter a card name: ")
        prices = api.get_price_by_name(name)
    elif "t" in choice:
        name = raw_input("Enter a tag: ")
        prices = api.get_price_by_name(name)

    if prices:
        print dumps(prices, indent=2)