# run_sweetshop.py
from src.sweetshop import SweetShop

def main():
    shop = SweetShop()

    # Add some sweets
    shop.add_sweet("Ladoo", 10, 100)
    shop.add_sweet("Rasgulla", 12, 50)
    shop.add_sweet("Barfi", 15, 30)

    print("Welcome to AI Kata Sweet Shop!")
    print("Available sweets:")
    for sweet, info in shop.sweets.items():
        print(f"{sweet}: Price ₹{info['price']}, Stock {info['stock']}")

    # Take order from user
    order = {}
    while True:
        sweet_name = input("Enter sweet name to buy (or 'done' to finish): ")
        if sweet_name.lower() == "done":
            break
        if sweet_name not in shop.sweets:
            print("Sweet not available!")
            continue
        qty = int(input(f"How many {sweet_name}? "))
        order[sweet_name] = qty

    if order:
        try:
            total = shop.place_order("Customer", order)
            print(f"Order successful! Total bill: ₹{total}")
            print("Remaining stock:")
            for sweet, info in shop.sweets.items():
                print(f"{sweet}: {info['stock']} left")
        except ValueError as e:
            print("Error:", e)
    else:
        print("No sweets ordered. Goodbye!")

if __name__ == "__main__":
    main()
