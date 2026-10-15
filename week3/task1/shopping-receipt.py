
def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 0)

        if price < 0 or quantity < 0:
            return False, "Price and quantity cannot be negative."

        subtotal += price * quantity

    return True, subtotal


def calculate_discount(subtotal):
    if subtotal < 0:
        return 0.0
    elif subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0.0


def calculate_tax(amount, tax_rate):
    if not 0 <= tax_rate <= 100:
        return False, "Tax rate must be between 0 and 100%."

    if amount < 0:
        return False, "Amount cannot be negative."

    return True, amount * (tax_rate / 100)


def generate_receipt(items, tax_rate):
    success, subtotal = calculate_subtotal(items)

    if not success:
        return subtotal

    discount = calculate_discount(subtotal)
    taxable_amount = subtotal - discount

    success, tax = calculate_tax(taxable_amount, tax_rate)

    if not success:
        return tax

    final_amount = taxable_amount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "taxable_amount": taxable_amount,
        "tax": tax,
        "final_amount": final_amount
    }


if __name__ == "__main__":
    items = [
        {"name": "Notebook", "price": 80, "quantity": 3},
        {"name": "Pen", "price": 15, "quantity": 5}
    ]

    tax_rate = 15

    receipt = generate_receipt(items, tax_rate)

    if isinstance(receipt, str):
        print(receipt)
    else:
        print("======= SHOPPING RECEIPT =======")

        for item in items:
            total = item["price"] * item["quantity"]
            print(
                f'{item["name"]}: {item["quantity"]} x '
                f'{item["price"]:.2f} = {total:.2f} Birr'
            )

        print("--------------------------------")
        print(f'Subtotal:      {receipt["subtotal"]:.2f} Birr')
        print(f'Discount:     -{receipt["discount"]:.2f} Birr')
        print(f'Taxable total: {receipt["taxable_amount"]:.2f} Birr')
        print(f'Tax ({tax_rate}%):     {receipt["tax"]:.2f} Birr')
        print(f'Final amount:  {receipt["final_amount"]:.2f} Birr')
        print("================================")
