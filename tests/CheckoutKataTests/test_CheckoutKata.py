from CheckoutKata import Checkout
import pytest

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("Kielbasa", 1)
    checkout.add_item_price("Makaron", 2)
    checkout.add_item_price("Pomodoro", 777)
    return checkout

##Removed due to duplicating
# def test_CanInstantiateCheckout():
#     co = Checkout()

# def test_add_item_price(checkout):
#     checkout.add_item_price("a", 1)

# def test_add_item(checkout):
#     checkout.add_item("Sausage")


def test_calculate_current_total(checkout):
    checkout.add_item("Kielbasa")
    assert checkout.calculate_total() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):

    checkout.add_item("Kielbasa")
    checkout.add_item("Makaron")
    assert checkout.calculate_total() == 3

def test_add_discount_rules(checkout):
    checkout.add_discount("Kielbasa", 3, 2)

def test_can_apply_discount_rule(checkout):
    for _ in range(4):
        checkout.add_item("Kielbasa")

    checkout.add_discount("Kielbasa", 3, 2)
    assert checkout.calculate_total() == 3

def test_exception_throw(checkout):
    with pytest.raises(Exception):
        checkout.add_item("Ziemniak")