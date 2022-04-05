#!/usr/bin/env python3

"""
Based of of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders: [('apples', 1.0), ('oranges', 3.0)] best shop is shop1.
For orders: [('apples', 3.0)] best shop is shop2.
"""

import shop

def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPound) tuples
    fruitShops: List of FruitShops
    """
    #first store in fruitShops to start iterating with
    first_store = fruitShops[0]

    #set cheapest store to first store
    cheapest_store = first_store

    #use get price to find cheapest price
    cheapest_price = first_store.getPriceOfOrder(orderList)

    #loop through all shops and test if it is cheaper. Return cheapest store
    for i in range(len(fruitShops)):
        fruit_shop = fruitShops[i]
        price = fruit_shop.getPriceOfOrder(orderList)
        if price < cheapest_price:
            cheapest_store = fruit_shop
            cheapest_price = price
    return cheapest_store




    return None

def main():
    dir1 = {
        'apples': 2.0,
        'oranges': 1.0
    }

    dir2 = {
        'apples': 1.0,
        'oranges': 5.0
    }

    shop1 = shop.FruitShop('shop1', dir1)
    shop2 = shop.FruitShop('shop2', dir2)

    shops = [shop1, shop2]

    orders = [('apples', 1.0), ('oranges', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

    orders = [('apples', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

if __name__ == '__main__':
    main()
