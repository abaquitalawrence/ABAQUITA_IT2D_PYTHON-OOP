from menu import MENU, display_menu


def get_quantity(item_name):
    while True:
        quantity_input = input(
            f"Enter quantity for {item_name}: "
        ).strip()

        try:
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            return quantity

        except ValueError:
            print(
                "Invalid quantity. "
                "Please enter a whole number."
            )


def take_order():
    orders = []

    while True:
        display_menu()

        choice = input(
            "Enter the menu number (0 to finish): "
        ).strip()

        if choice == "0":

            if not orders:
                print("\nNo items were ordered.")

                confirm = input(
                    "Do you want to exit? (yes/no): "
                ).strip().lower()

                if confirm in ("yes", "y"):
                    return orders

                continue

            return orders

        if choice not in MENU:
            print(
                "Invalid menu number. "
                "Please choose an item from the menu."
            )
            continue

        quantity = get_quantity(MENU[choice]["name"])

        item = MENU[choice]

        order = {
            "name": item["name"],
            "quantity": quantity,
            "price": item["price"],
            "subtotal": item["price"] * quantity
        }

        orders.append(order)

        print(
            f"Added {quantity} x {item['name']} "
            f"= PHP {order['subtotal']:.2f}"
        )

        while True:
            another = input(
                "Do you want to order another item? (yes/no): "
            ).strip().lower()

            if another in ("yes", "y"):
                break

            if another in ("no", "n"):
                return orders

            print("Please enter yes or no.")