from shoppingcart.cart import ShoppingCart
from tests import test_cart
import sys
import os

print(os.path.dirname(__file__))

rec = test_cart.test_add_different_items()
print(rec)
test_cart.test_add_different_items_Currency('USD')

print('done')
