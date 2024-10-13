

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

    if item_counts['E'] > 0:
        total += (item_counts['E'] // 2) * prices['E'] * 2
        total += (item_counts['E'] % 2) * prices['E']
        free_b_count = min(item_counts['B'], item_counts['E'] // 2)
        item_counts['B'] -= free_b_count

    if item_counts['B'] > 0:
        offer_qty, offer_price = special_offers['B']
        total += (item_counts['B'] // offer_qty) * offer_price
        total += (item_counts['B'] % offer_qty) * prices['B']

    if item_counts['A'] > 0:
        for offer_qty, offer_price in special_offers['A']:
            total += (item_counts['A'] // offer_qty) * offer_price
            item_counts['A'] %= offer_qty
        total += item_counts['A'] * prices['A']

    total += item_counts['C'] * prices['C']
    total += item_counts['D'] * prices['D']

    return total

#==============================================================================

def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
    }

    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': (2, 45),
    }

    item_counts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0
    }

    total = 0

    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] += 1

    if item_counts['E'] > 0:
        total += (item_counts['E'] // 2) * prices['E'] * 2
        total += (item_counts['E'] % 2) * prices['E']
        free_b_count = min(item_counts['B'], item_counts['E'] // 2)
        item_counts['B'] -= free_b_count

    if item_counts['B'] > 0:
        offer_qty, offer_price = special_offers['B']
        total += (item_counts['B'] // offer_qty) * offer_price
        total += (item_counts['B'] % offer_qty) * prices['B']

    if item_counts['A'] > 0:
        for offer_qty, offer_price in special_offers['A']:
            total += (item_counts['A'] // offer_qty) * offer_price
            item_counts['A'] %= offer_qty
        total += item_counts['A'] * prices['A']

    if item_counts['F'] > 0:
        total += (item_counts['F'] // 3) * prices['F'] * 2
        total += (item_counts['F'] % 3) * prices['F']

    total += item_counts['C'] * prices['C']
    total += item_counts['D'] * prices['D']

    return total

#=================================================================
def checkout(skus):
    prices = {
        'A': 50,  'B': 30,  'C': 20,  'D': 15,  'E': 40,  'F': 10,  'G': 20,
        'H': 10,  'I': 35,  'J': 60,  'K': 80,  'L': 90,  'M': 15,  'N': 40,
        'O': 10,  'P': 50,  'Q': 30,  'R': 50,  'S': 30,  'T': 20,  'U': 40,
        'V': 50,  'W': 20,  'X': 90,  'Y': 10,  'Z': 50
    }

    special_offers = {
        'A': [(5, 200), (3, 130)],
        'B': (2, 45),
        'H': [(10, 80), (5, 45)],
        'K': (2, 150),
        'P': (5, 200),
        'Q': (3, 80),
        'V': [(3, 130), (2, 90)],
    }

    free_item_offers = {
        'E': ('B', 2),
        'N': ('M', 3),
        'R': ('Q', 3),
        'F': ('F', 2),
        'U': ('U', 3),
    }

    item_counts = {item: 0 for item in prices}

    total = 0

    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] += 1

    for offer_item, (free_item, required_count) in free_item_offers.items():
        if item_counts[offer_item] > 0:
            free_count = item_counts[offer_item] // (required_count + 1)
            item_counts[free_item] = max(0, item_counts[free_item] - free_count)

    for item, count in item_counts.items():
        if item in special_offers:
            offers = special_offers[item]
            if isinstance(offers, list):
                for offer_qty, offer_price in offers:
                    total += (count // offer_qty) * offer_price
                    count %= offer_qty
            else:
                total += (count // offers[0]) * offers[1]
                count %= offers[0]

        total += count * prices[item]

    return total


