
print("--- The Movie Ticket Pricer ---")
 
age = int(input('Please enter your age: '))
if age <= 12:
    print('You fall into the "Children" age')
    print('The price is: $8')
elif age <= 64:
    print('You fall into the "Adult" age')
    print('The price is: $15')
else:
    print('You fall into the "Seniors" age')
    print('The price is: $10')