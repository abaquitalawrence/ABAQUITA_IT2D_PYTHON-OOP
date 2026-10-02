def calculate_total(orders):
    subtotal = 0.00

    for order in orders:
        subtotal += order["subtotal"]

    # 10% discount if subtotal reaches PHP 500
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0.00

    total = subtotal - discount

    return subtotal, discount, total