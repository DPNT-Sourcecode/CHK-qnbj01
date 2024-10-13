

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    special_offers = {
        'A': (3, 130),
        'B': (2, 45)
    }

    item_counts = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0
    }

    total = 0

    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] += 1

    for item, count in item_counts.items():
    if item in special_offers:
        offer_qty, offer_price = special_offers[item]
        total += (count // offer_qty) * offer_price
        total += (count % offer_qty) * prices[item]
    else:
        total += count * prices[item]

return total




