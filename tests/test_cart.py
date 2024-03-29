from shoppingcart.cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item('apple', 1)

    receipt = cart.print_receipt()

    assert receipt[0] == 'apple - 1 - €1.00'


def test_add_item_with_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item('apple', 2)

    receipt = cart.print_receipt()

    assert receipt[0] == 'apple - 2 - €2.00'


def test_add_different_items():
    cart = ShoppingCart()
    cart.add_item('banana', 1)
    cart.add_item('kiwi', 1)

    receipt = cart.print_receipt()
    
    assert receipt[0] == 'banana - 1 - €1.10'
    assert receipt[1] == 'kiwi - 1 - €3.00'

    return receipt

def test_add_different_items_Currency(curr):
    cart = ShoppingCart()
    cart.add_item('apple', 1)
    cart.add_item('kiwi', 1)

    receipt = cart.print_receipt(curr)

    print(receipt)
    """ assert receipt[0].startswith('apple -1 - %s' curr)
    assert receipt[1].startswith('kiwi - 1 - %s' curr) """
    
# if __name__ == '__main__':
#     test_add_different_items_Currency('USD')
