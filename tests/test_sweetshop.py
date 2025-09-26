import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sweetshop import SweetShop


def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet("Ladoo", 10, 100)
    assert shop.sweets["Ladoo"]["price"] == 10
    assert shop.sweets["Ladoo"]["stock"] == 100

def test_place_order():
    shop = SweetShop()
    shop.add_sweet("Ladoo", 10, 100)
    bill = shop.place_order("Sachin", {"Ladoo": 5})
    assert bill == 50
    assert shop.sweets["Ladoo"]["stock"] == 95

def test_order_not_available():
    shop = SweetShop()
    shop.add_sweet("Rasgulla", 12, 50)
    try:
        shop.place_order("Sachin", {"Ladoo": 1})
    except ValueError as e:
        assert str(e) == "Ladoo not available"

def test_order_insufficient_stock():
    shop = SweetShop()
    shop.add_sweet("Barfi", 15, 3)
    try:
        shop.place_order("Sachin", {"Barfi": 5})
    except ValueError as e:
        assert str(e) == "Not enough stock for Barfi"
