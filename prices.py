import requests


class YGOPricesAPI():

    def __init__(self):
        self.url = "http://yugiohprices.com/api/"

    def __make_request(self, url):
        """Request a resource from api"""
        request = requests.get(url)

        if request.status_code != 200:
            print(request)
            print("Request status not OK. Returning None...")
            return

        return request.json()

    def get_price_by_name(self, name):
        """Retrieves price data for every version of a card using its name"""
        url = self.url + "get_card_prices/" + name
        return self.__make_request(url)

    def get_price_by_tag(self, tag, rarity=None):
        """Retrieve price data for a specific version of a card using its print tag"""
        url = self.url
        if rarity:
            url += "price_history/" + tag + "?rarity=" + rarity
            print(url)
        else:
            url += "price_for_print_tag/" + tag
        return self.__make_request(url)

    def get_set_data(self, set_name):
        """Returns rarities and low/high/average prices for each card in the set."""
        url = self.url + "set_data/" + set_name
        return self.__make_request(url)

    def get_sets(self):
        """Retrieve list of all set names in Yugioh Prices database"""
        url = self.url + "card_sets"
        return self.__make_request(url)

    def get_rising_and_falling(self):
        """Retrieve rising and falling cards list"""
        url = self.url + "rising_and_falling"
        return self.__make_request(url)

    def get_top_100(self, rarity=None):
        """Retrieve Top 100 most expensive cards"""
        url = self.url + "top_100_cards"
        if rarity:
            url += "?rarity=" + rarity
        return self.__make_request(url)

    def get_card_names(self):
        """Retrieve all cards name"""
        url = self.url + "card_names"
        return self.__make_request(url)

    def get_card_data(self, name):
        """Retrieve all information for a card using its name"""
        url = self.url + "card_data/" + name
        return self.__make_request(url)

    def get_card_versions(self, name):
        """Retrieve a list of all known versions of a card using its name"""
        url = self.url + "card_versions/" + name
        return self.__make_request(url)

    def get_card_support(self, name):
        """Retrieve a list of support cards for a given card using its name"""
        url = self.url + "card_support/" + name
        return self.__make_request(url)
