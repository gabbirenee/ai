# Gabbi Forsythe
# 2/10/2020
# Project #1: Question #3

# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    # my code below
    bestShop = None
    bestPrice = 1000000.0
    for fruitShop in fruitShops:
        price = fruitShop.getPriceOfOrder(orderList)
        if price < bestPrice:
            bestShop = fruitShop
            bestPrice = price
        
    return bestShop


if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())

# AUTOGRADING
# thomas% python3 autograder.py -q q3
# Starting on 2-5 at 15:08:06

# Question q3
# ===========

# Welcome to shop1 fruit shop
# Welcome to shop2 fruit shop
# *** PASS: test_cases/q3/select_shop1.test
# *** 	shopSmart(order, shops) selects the cheapest shop
# Welcome to shop1 fruit shop
# Welcome to shop2 fruit shop
# *** PASS: test_cases/q3/select_shop2.test
# *** 	shopSmart(order, shops) selects the cheapest shop
# Welcome to shop1 fruit shop
# Welcome to shop2 fruit shop
# Welcome to shop3 fruit shop
# *** PASS: test_cases/q3/select_shop3.test
# *** 	shopSmart(order, shops) selects the cheapest shop

# ### Question q3: 1/1 ###


# Finished at 15:08:06

# Provisional grades
# ==================
# Question q3: 1/1
# ------------------
# Total: 1/1

# Your grades are NOT yet registered.  To register your grades, make sure
# to follow your instructor's guidelines to receive credit on your project.

# thomas% 