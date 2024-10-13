

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

#===========================================================================


def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': (2, 45)
    }

    item_counts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }

    total = 0

    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] += 1

    for item, count in item_counts.items():
        if item == 'A':
            for offer_qty, offer_price in special_offers['A']:
                total += (count // offer_qty) * offer_price
                count %= offer_qty
            total += count * prices['A']

        elif item == 'B':
            offer_qty, offer_price = special_offers['B']
            total += (count // offer_qty) * offer_price
            total += (count % offer_qty) * prices['B']

        elif item == 'E':
            total += (count // 2) * prices['E'] * 2
            total += (count % 2) * prices['E']
            free_b_count = min(item_counts['B'], count // 2)
            item_counts['B'] -= free_b_count

        else:
            total += count * prices[item]

        if item_counts['B'] > 0:
            total += item_counts['B'] * prices['B']

    return total

