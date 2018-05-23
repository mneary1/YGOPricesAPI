# YGOPricesAPI

A Python wrapper around the yugiohprices.com API.

Usage:

```
from prices import YGOPricesAPI
api = YGOPricesAPI()
```

## get_price_by_name

### Retrieves price data for every version of a card using its name
```
>>> api.get_price_by_name('Blue-Eyes White Dragon')
```

## get_price_by_tag

### Retrieve price data for a specific version of a card using its print tag
```
>>> api.get_price_by_tag('YSKR-EN001', rarity='Secret Rare')
```

## get_set_data

### Returns rarities and low/high/average prices for each card in the set.
```
>>> api.get_set_data('Legend of Blue Eyes White Dragon')
```

## get_sets

### Retrieve list of all set names in Yugioh Prices database
```
>>> api.get_sets()
```
        
## get_rising_and_falling()

### Retrieve rising and falling cards list
```
>>> api.get_rising_and_falling()
```
        
## get_top_100(rarity=None)

### Retrieve Top 100 most expensive cards
```
>>> api.get_top_100(rarity='Secret Rare')
```
        
## get_card_names()

### Retrieve all cards name
```
>>> api.get_card_names()
```
        
## get_card_data(name)

### Retrieve all information for a card using its name
```
>>> api.get_card_data('Blue-Eyes White Dragon')
```
        
## get_card_versions(name)

### Retrieve a list of all known versions of a card using its name
```
>>> api.get_card_versions('Blue-Eyes White Dragon')
```
        
## get_card_support(name)

### Retrieve a list of support cards for a given card using its name
```
>>> api.get_card_support('Blue-Eyes White Dragon')
```