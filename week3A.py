print('=== Pet Grooming Service Calculator ===')
print('Enter service package: bath, trim, or full')
print('Type "done" when finished selecting services')
 
subtotal=0
while True:
    package=input('Enter service package: ')
    if package=="done":
        break
    elif package=='bath':
        price=15
        subtotal=subtotal+price
        print(f'Price: ${price: .2f}')
        print(f"Current total: ${subtotal: .2f}")
    elif package=="trim":
        price=25
        subtotal=subtotal+price
        print(f"Price: ${price: .2f}")
        print(f"Current total: ${subtotal: .2f}")
    elif package=="full":
        price=40
        subtotal=subtotal+price
        print(f"Price: ${price: .2f}")
        print(f"Current total: ${subtotal: .2f}")
if subtotal>=75:
    saving=12
    total=subtotal-saving
else:
    saving=0
    total=subtotal
print("\n=== Service Summary ===")
print(f"Subtotal: ${subtotal: .2f}")
print(f"Multi-Pet Discount: -${saving: .2f}")
print(f"Final Total: ${total: .2f}")
print("Thank you for choosing our salon!")