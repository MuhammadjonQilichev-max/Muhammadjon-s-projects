print("--- Triangle Pattern Printer ---")
h = int(input('Enter the height of the triangle: '))
w = 1

for row_num in range(h):

    for col_num in range(w+row_num):

        print("*  ", end="")

    print()

