dish1 = input("Enter the name of the first dish: ")
price1 = float(input("Enter the price of the first dish: "))
quantity1 = int(input("Enter the quantity of the first dish: "))

dish2 = input("Enter the name of the second dish: ")
price2 = float(input("Enter the price of the second dish: "))
quantity2 = int(input("Enter the quantity of the second dish: "))

dish3 = input("Enter the name of the third dish: ")
price3 = float(input("Enter the price of the third dish: "))
quantity3 = int(input("Enter the quantity of the third dish: "))

print("\n--- Customer Information ---")
customer_name = input("Enter your name: ")
has_student_id = input("Do you have a student ID? (yes/no): ") == "yes"
order_time = float(input("Order time (hour in 24-hour format): "))

subtotal = (price1 * quantity1 + price2 * quantity2 + price3 * quantity3)

student_eligible = has_student_id
happy_hour_eligible = (order_time >= 14) * (order_time <= 17)
large_order_eligible = subtotal >= 150000

student_discount = 0.15 * subtotal * student_eligible
happy_hour_discount = 0.20 * subtotal * happy_hour_eligible

main_discount = (student_discount * (student_discount >= happy_hour_discount) + happy_hour_discount * (happy_hour_discount > student_discount))

large_order_discount = 0.05 * subtotal * large_order_eligible

total_discounts = main_discount + large_order_discount
subtotal_after_discounts = subtotal - total_discounts

service_charge = 0.10 * subtotal_after_discounts

delivery_fee = (subtotal >= 100000) * 15000
free_delivery = delivery_fee == 0

final_total = subtotal_after_discounts + service_charge + delivery_fee
total_saved = total_discounts

print("\n========== ORDER SUMMARY ==========")
print(f"Customer Name       : {customer_name}")
print(f"Student ID Provided : {student_eligible}")
print(f"Order Time          : {order_time}:00")

print("\n--- Ordered Items ---")
print(f"{dish1} - {quantity1} x {price1} = {price1 * quantity1}")
print(f"{dish2} - {quantity2} x {price2} = {price2 * quantity2}")
print(f"{dish3} - {quantity3} x {price3} = {price3 * quantity3}")

print(f"\nSubtotal (Before Discounts): {subtotal:.0f} sum")

print("\n--- Discounts ---")
print(f"Student Discount Eligible : {bool(student_eligible)} | Amount: {student_discount:.0f} sum")
print(f"Happy Hour Eligible       : {bool(happy_hour_eligible)} | Amount: {happy_hour_discount:.0f} sum")

applied_discount_type = (
    "Student Discount" * (student_discount >= happy_hour_discount)
    + "Happy Hour Discount" * (happy_hour_discount > student_discount)
)

print(f"Applied Discount          : {applied_discount_type} | Amount: {main_discount:.0f} sum")
print(f"Large Order Eligible      : {bool(large_order_eligible)} | Amount: {large_order_discount:.0f} sum")
print(f"Total Discounts Applied   : {total_discounts:.0f} sum")

print("\n--- After Discounts ---")
print(f"Subtotal After Discounts  : {subtotal_after_discounts:.0f} sum")
print(f"Service Charge (10%)      : {service_charge:.0f} sum")
print(f"Delivery Fee              : {delivery_fee:.0f} sum (Free Delivery: {bool(free_delivery)})")

print("\n--- FINAL TOTAL ---")
print(f"Final Amount to Pay       : {final_total:.0f} sum")
print(f"Total Amount Saved        : {total_saved:.0f} sum")
print("==================================")
