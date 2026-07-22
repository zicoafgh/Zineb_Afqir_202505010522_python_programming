def get_customer():

    print("=== Customer Information ===")

    name = input("Customer Name : ")
    food = input("Food Ordered (Cake/Muffin) : ")
    quantity = int(input("Quantity : "))
    price = 3.00

    delivery = input("Delivery (Y/N): ")

    if delivery.upper() == "Y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00

    return name, food, quantity, price, delivery_charges