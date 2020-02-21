# Gabbi Forsythe
# 2/10/2020
# Project #1: Question #2

# buyLotsOfFruit.py
# -----------------
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
To run this script, type

  python buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""
from __future__ import print_function

fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """
    # My code Below
    totalCost = 0.0
    for fruit, numPounds in orderList:
        if fruit not in fruitPrices:
            print('Error')
            return None
        else:
            totalCost += numPounds * fruitPrices[fruit]
    return totalCost


# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))

# AUTOGRADING
# thomas% python3 autograder.py -q q2
# Starting on 2-5 at 15:06:20

# Question q2
# ===========

# *** PASS: test_cases/q2/food_price1.test
# *** 	buyLotsOfFruit correctly computes the cost of the order
# *** PASS: test_cases/q2/food_price2.test
# *** 	buyLotsOfFruit correctly computes the cost of the order
# *** PASS: test_cases/q2/food_price3.test
# *** 	buyLotsOfFruit correctly computes the cost of the order

# ### Question q2: 1/1 ###


# Finished at 15:06:20

# Provisional grades
# ==================
# Question q2: 1/1
# ------------------
# Total: 1/1

# Your grades are NOT yet registered.  To register your grades, make sure
# to follow your instructor's guidelines to receive credit on your project.

# thomas% 