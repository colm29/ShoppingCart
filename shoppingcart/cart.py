import typing
from collections import OrderedDict
import json
import sys
import os
from pathlib import Path

from . import abc
from .helpers.currency import getCurr


class ShoppingCart(abc.ShoppingCart):
    def __init__(self):
        self._items = OrderedDict()
        self._prices = dict()
        # <-- absolute dir the script is in
        script_dir = os.path.dirname(__file__)
        json_path = Path('json/prices.json')
        abs_file_path = os.path.join(script_dir, json_path)
        self._prices = json.loads(open(abs_file_path, 'r').read())

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity

    def print_receipt(self, curr: str = 'EUR') -> typing.List[str]:
        lines = []
        total = 0.00
        currSymbol = '€'

        if curr != 'EUR':
            currSymbol = curr
            rate = getCurr(curr)
        else:
            rate = 1

        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1] * rate
            total += price
            price_string = currSymbol + '%.2f' % price

            lines.append(item[0] + ' - ' + str(item[1]) + ' - ' + price_string)

        lines.append('Total: ' + currSymbol + '%.2f' % total)

        return lines

    def _get_product_price(self, product_code: str) -> float:
        price = 0.0

        if product_code == 'apple':
            price = self._prices['apple']

        elif product_code == 'banana':
            price = self._prices['banana']

        elif product_code == 'kiwi':
            price = self._prices['kiwi']

        return price
