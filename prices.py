import requests

class YGOPriceAPI():
    def __init__(self):
        self.url = "http://yugiohprices.com/api/"

    def __make_request(self, url):
        request = requests.get(url)
        
        if request.status_code != 200:
            print request
            print "Request status not OK. Returning None..."
            return 

        return request.json()

    def get_price_by_name(self, name):
        url = self.url + "get_card_prices/" + name  
        return self.__make_request(url)

    def get_price_by_tag(self, tag, rarity=None):
        url = self.url 
        if rarity:
            url += "price_history/" + tag + "?rarity=" + rarity
            print url
        else:
            url += "price_for_print_tag/" + tag
        return self.__make_request(url)

    def get_set_data(self, set_name):
        url = self.url + "set_data/" + set_name
        return self.__make_request(url)
    
    def get_sets(self):
        url = self.url + "card_sets"
        return self.__make_request(url)

    
