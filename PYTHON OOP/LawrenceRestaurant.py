# LAWRENCE RESTAURANT
# Python OOP Version
# Based on the Prelim Restaurant Ordering System


class MenuItem:
    """Represents one item in the restaurant menu."""

    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price


class Menu:
    """Manages the restaurant menu."""

    def __init__(self):
        self.items = [
            MenuItem("1", "Cheeseburger", 89.00),
            MenuItem("2", "Chicken Sandwich", 99.00),
            MenuItem("3", "French Fries", 59.00),
            MenuItem("4", "Chicken Nuggets", 79.00),
            MenuItem("5", "Soft Drink", 39.00),
            MenuItem("6", "Iced Tea", 49.00)
        ]

    def display_menu(self):
        print("\n" + "=" * 55)
        print("              LAWRENCE RESTAURANT")
        print("=" * 55)
        print(f"{'No.':<6}{'Menu Item':<30}{'Price':>12}")
        print("-" * 55)

        for item in self.items:
            print(
                f"{item.number:<6}"
                f"{item.name:<30}"
                f"PHP {item.price:>7.2f}"
            )

        print("-" * 55)
        print("0     Finish ordering")
        print("=" * 55)

    def find_item(self, number):
        for item in self.items:
            if item.number == number:
                return item

        return None


class OrderItem:
    """Represents an item ordered by the customer."""

    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_subtotal(self):
        return self.menu_item.price * self.quantity


class Order:
    """Manages the customer's complete order."""

    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        order_item = OrderItem(menu_item, quantity)
        self.items.append(order_item)

    def is_empty(self):
        return len(self.items) == 0

    def calculate_subtotal(self):
        subtotal = 0.00

        for item in self.items:
            subtotal += item.get_subtotal()

        return subtotal

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()

        # 10% discount if subtotal reaches PHP 500
        if subtotal >= 500:
            return subtotal * 0.10

        return 0.00

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()

        return subtotal - discount


class Receipt:
    """Displays the customer's sales receipt."""

    def print_receipt(self, order):
        subtotal = order.calculate_subtotal()
        discount = order.calculate_discount()
        total = order.calculate_total()

        print("\n" + "=" * 65)
        print("                    LAWRENCE RESTAURANT")
        print("                       SALES RECEIPT")
        print("=" * 65)

        print(
            f"{'Item':<25}"
            f"{'Qty':>6}"
            f"{'Price':>14}"
            f"{'Amount':>15}"
        )

        print("-" * 65)

        for item in order.items:
            print(
                f"{item.menu_item.name:<25}"
                f"{item.quantity:>6}"
                f"PHP {item.menu_item.price:>9.2f}"
                f"PHP {item.get_subtotal():>10.2f}"
            )

        print("-" * 65)

        print(
            f"{'Subtotal':>49} "
            f"PHP {subtotal:>10.2f}"
        )

        print(
            f"{'Discount':>49} "
            f"PHP {discount:>10.2f}"
        )

        print(
            f"{'TOTAL':>49} "
            f"PHP {total:>10.2f}"
        )

        print("=" * 65)
        print("           Thank you for dining with us!")
        print("=" * 65)


class Restaurant:
    """Controls the complete restaurant ordering process."""

    def __init__(self):
        self.menu = Menu()
        self.receipt = Receipt()

    def get_quantity(self, item_name):
        """Gets and validates the customer's quantity."""

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

    def take_order(self):
        """Gets the customer's order."""

        order = Order()

        while True:
            self.menu.display_menu()

            choice = input(
                "Enter the menu number (0 to finish): "
            ).strip()

            # Finish ordering
            if choice == "0":

                if order.is_empty():
                    print("\nNo items were ordered.")

                    confirm = input(
                        "Do you want to exit? (yes/no): "
                    ).strip().lower()

                    if confirm in ("yes", "y"):
                        return order

                    continue

                return order

            # Find selected menu item
            menu_item = self.menu.find_item(choice)

            if menu_item is None:
                print(
                    "Invalid menu number. "
                    "Please choose an item from the menu."
                )
                continue

            # Get quantity
            quantity = self.get_quantity(menu_item.name)

            # Add item to order
            order.add_item(menu_item, quantity)

            subtotal = menu_item.price * quantity

            print(
                f"Added {quantity} x {menu_item.name} "
                f"= PHP {subtotal:.2f}"
            )

            # Ask if customer wants another item
            while True:
                another = input(
                    "Do you want to order another item? (yes/no): "
                ).strip().lower()

                if another in ("yes", "y"):
                    break

                if another in ("no", "n"):
                    return order

                print("Please enter yes or no.")

    def run(self):
        """Runs the restaurant system."""

        print("=" * 55)
        print("       WELCOME TO LAWRENCE RESTAURANT")
        print("=" * 55)
        print(
            "Please choose from our menu "
            "and enjoy your meal!"
        )

        order = self.take_order()

        # No order
        if order.is_empty():
            print(
                "\nThank you for visiting "
                "Lawrence Restaurant!"
            )
            print("Have a great day!")
            return

        # Display receipt
        self.receipt.print_receipt(order)

        # Display final amount
        total = order.calculate_total()

        print(
            f"\nFinal amount to pay: "
            f"PHP {total:.2f}"
        )

        print("Order completed successfully.")


# Main Program
def main():
    restaurant = Restaurant()
    restaurant.run()


if __name__ == "__main__":
    main()