print("--- The running total calculator ---")
print("Enter numbers to add them up. Type 'done' to see the total.")
total=0
while True:
    number = input('Enter number or type "done" to see the total: ')
    if number == 'done':
        break
    number=float(number)
    total+=number
print('Current total: ',total)


