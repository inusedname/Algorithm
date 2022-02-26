#!/bin/python3

import math
import os
import random
import re
import sys


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        pass
    pass


class ShoppingCart:
    Cart = []

    def __init__(self) -> None:
        pass

    def add(self, something):
        flag = 0
        for i in self.Cart:
            if i[0] == something:
                flag = 1
                i[1] += 1
        if flag == 0:
            self.Cart.append([something, 1])

    def total(self):
        sum = 0
        for i in self.Cart:
            sum = sum + i[0].price * i[1]
        return sum


def len(something):
    res = 0
    for i in something.Cart:
        res += i[1]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)

    fptr.close()
