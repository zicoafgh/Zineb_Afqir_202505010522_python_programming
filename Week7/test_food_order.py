from food_order import calculate_order

def test_order1():
    assert calculate_order(10, 2) == 20

def test_order2():
    assert calculate_order(10, 3) == 30

def test_order3():
    assert calculate_order(50, 2) == 100

def test_order4():
    assert calculate_order(5, 2) == 10

def test_invalid_price():
    assert calculate_order(-5, 2) == "invalid price"

def test_invalid_quantity():
    assert calculate_order(5, -2) == "invalid quantity"
   

