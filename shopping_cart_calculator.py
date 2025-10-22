def calculate_item_total(quantity, unit_price):
    total = quantity * unit_price
    return total
def apply_bulk_discount(total, quantity):
    if quantity >= 10:
        return total * 10 / 100
    elif quantity >= 5:
        return total * 0.05
    else:
        return 0
def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate / 100
def is_eligible_for_free_shipping(subtotal):
    return subtotal >= 50
def process_order(item_name, quantity, unit_price, tax_rate):

    item_total = calculate_item_total(quantity, unit_price)

    discount = apply_bulk_discount(item_total, quantity)
    subtotal = item_total - discount
    tax = calculate_tax(subtotal, tax_rate)
    is_eligible = is_eligible_for_free_shipping(subtotal)
    print('--- receipt ----')
    print(f'{item_name}: {unit_price} x {quantity} = {item_total}')
    print(f'Discount: {discount}')
    print(f'Subtotal: {subtotal}')
    print(f'Tax: {tax}')
    print(f'Is Eligible for free shipping: {is_eligible}')
process_order("Computer", 5, 2000000, 10)