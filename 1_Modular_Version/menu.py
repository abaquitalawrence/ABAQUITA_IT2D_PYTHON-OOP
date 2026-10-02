MENU = {
    "1": {"name": "Cheeseburger", "price": 89.00},
    "2": {"name": "Chicken Sandwich", "price": 99.00},
    "3": {"name": "French Fries", "price": 59.00},
    "4": {"name": "Chicken Nuggets", "price": 79.00},
    "5": {"name": "Soft Drink", "price": 39.00},
    "6": {"name": "Iced Tea", "price": 49.00},
}


def display_menu():
    print("\n" + "=" * 55)
    print("              LAWRENCE RESTAURANT")
    print("=" * 55)
    print(f"{'No.':<6}{'Menu Item':<30}{'Price':>12}")
    print("-" * 55)

    for item_number, item in MENU.items():
        print(
            f"{item_number:<6}"
            f"{item['name']:<30}"
            f"PHP {item['price']:>7.2f}"
        )

    print("-" * 55)
    print("0     Finish ordering")
    print("=" * 55)