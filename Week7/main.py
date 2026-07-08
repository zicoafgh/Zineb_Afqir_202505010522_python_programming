from food_order import calculate_order 
def main():
    price= float(input("Price(RM)":))
    quantity = int(input("Quantity :"))

    total = calculate_order(price,quantity)

    print(f"Total payment = RM {total:.2f}")

    if __name__ == "__main__":
       main()