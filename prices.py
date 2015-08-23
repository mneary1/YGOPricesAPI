import requests

class YGOPriceAPI():
    def __init__(self):
        self.url = "http://yugiohprices.com/api/"

    def get_price_by_name(self, name):
        url = self.url + "get_card_prices/" + name  
        return __make_request(url)

    def get_price_by_tag(self, tag):
        url = self.url + "price_for_print_tag/" + tag
        return __make_request(url)

    def __make_request(self, url):
        request = requests.get(url)
        
        if request.status_code != 200:
            print request
            print "Request status not OK. Returning None..."
            return 
        
        json_response = request.json()
        if json_response['status'] == "fail":
            print json_response['message']
            return

        return json_response