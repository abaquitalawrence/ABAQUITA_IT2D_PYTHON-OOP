from ordering import take_order
from calculation import calculate_total
from receipt import print_receipt


def main():
    print("=" * 55)
    print("       WELCOME TO LAWRENCE RESTAURANT")
    print("=" * 55)
    print(
        "Please choose from our menu "
        "and enjoy your meal!"
    )

    orders = take_order()

    if not orders:
        print(
            "\nThank you for visiting "
            "Lawrence Restaurant!"
        )
        print("Have a great day!")
        return

    subtotal, discount, total = calculate_total(orders)

    print_receipt(
        orders,
        subtotal,
        discount,
        total
    )

    print(
        f"\nFinal amount to pay: "
        f"PHP {total:.2f}"
    )

    print("Order completed successfully.")


if __name__ == "__main__":
    main()