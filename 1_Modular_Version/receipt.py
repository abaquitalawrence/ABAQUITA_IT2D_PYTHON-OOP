def print_receipt(orders, subtotal, discount, total):
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

    for order in orders:
        print(
            f"{order['name']:<25}"
            f"{order['quantity']:>6}"
            f"PHP {order['price']:>9.2f}"
            f"PHP {order['subtotal']:>10.2f}"
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