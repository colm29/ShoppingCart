import typing
from collections import OrderedDict
import json

from . import abc


class ShoppingCart(abc.ShoppingCart):
    def __init__(self):
        self._items = OrderedDict()
        self._PRICES = dict()

        self._PRICES = json.loads(open('prices.json', 'r').read())

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity

    def print_receipt(self) -> typing.List[str]:
        lines = []
        total = 0.00
        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1]
            total += price
            price_string = "€%.2f" % price

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)
        lines.append("Total: €%s" % total )

        return lines

    def _get_product_price(self, product_code: str) -> float:
        price = 0.0

        if product_code == 'apple':
            price = self._PRICES['apple']

        elif product_code == 'banana':
            price = self._PRICES['banana']

        elif product_code == 'kiwi':
            price = self._PRICES['kiwi']

        return price
