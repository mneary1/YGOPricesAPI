# YGOPricesAPI
A Python wrapper around the yugiohprices.com API.
I wanted to build an application using the yugiohprices.com API, but there weren't any wrappers for it.

So I wrote one.

Usage:

```
from prices import YGOPricesAPI
api = YGOPricesAPI()
# make api call
# all api calls return the json response 
# Ex:
price = api.get_price_by_name("Blue-eyes White Dragon")
```

