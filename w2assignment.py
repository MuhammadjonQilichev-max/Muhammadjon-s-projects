# ==========================
# RESTAURANT ORDER CALCULATOR
# ==========================

# --- Collect order data for 3 dishes ---
dishes = []
for i in range(1, 4):
    print(f"\nEnter details for Dish {i}:")
    name = input("Dish name: ")
    price = int(input("Price (sum): "))
    quantity = int(input("Quantity: "))
    dishes.append({"name": name, "price": price, "quantity": quantity})

# --- Get customer info ---
print("\n--- Customer Information ---")
customer_name = input("Customer name: ")
has_student_id = input("Do you have a student ID? (yes/no): ").strip().lower() == "yes"
order_time = int(input("Order time (hour in 24-hour format): "))

# --- Subtotal before discounts ---
subtotal = sum(d["price"] * d["quantity"] for d in dishes)

# --- Discount calculations ---
# 1. Student discount
student_eligible = has_student_id
student_discount = 0.15 * subtotal if student_eligible else 0

# 2. Happy hour discount
happy_hour_eligible = 14 <= order_time <= 17
happy_hour_discount = 0.20 * subtotal if happy_hour_eligible else 0

# 3. Non-stacking rule (choose better discount)
if student_discount >= happy_hour_discount:
    main_discount = student_discount
    applied_discount_type = "Student Discount"
else:
    main_discount = happy_hour_discount
    applied_discount_type = "Happy Hour Discount"

# 4. Large order discount (stacks with main discount)
large_order_eligible = subtotal >= 150000
large_order_discount = 0.05 * subtotal if large_order_eligible else 0

# --- Total discounts ---
total_discounts = main_discount + large_order_discount
subtotal_after_discounts = subtotal - total_discounts

# --- Service charge (10% of subtotal after discounts) ---
service_charge = 0.10 * subtotal_after_discounts

# --- Delivery fee ---
delivery_fee = 15000 if subtotal >= 100000 else 0
free_delivery = delivery_fee == 0

# --- Final total ---
final_total = subtotal_after_discounts + service_charge + delivery_fee

# --- Total amount saved ---
total_saved = total_discounts

# ==========================
# OUTPUT SECTION
# ==========================

print("\n========== ORDER SUMMARY ==========")
print(f"Customer Name       : {customer_name}")
print(f"Student ID Provided : {student_eligible}")
print(f"Order Time          : {order_time}:00")
print("\n--- Ordered Items ---")
for d in dishes:
    print(f"{d['name']} - {d['quantity']} x {d['price']} = {d['quantity'] * d['price']} sum")

print(f"\nSubtotal (Before Discounts): {subtotal:,} sum")

print("\n--- Discounts ---")
print(f"Student Discount Eligible : {student_eligible} | Amount: {int(student_discount):,} sum")
print(f"Happy Hour Eligible       : {happy_hour_eligible} | Amount: {int(happy_hour_discount):,} sum")
print(f"Applied Discount          : {applied_discount_type} | Amount: {int(main_discount):,} sum")
print(f"Large Order Eligible      : {large_order_eligible} | Amount: {int(large_order_discount):,} sum")
print(f"Total Discounts Applied   : {int(total_discounts):,} sum")

print("\n--- After Discounts ---")
print(f"Subtotal After Discounts  : {int(subtotal_after_discounts):,} sum")
print(f"Service Charge (10%)      : {int(service_charge):,} sum")
print(f"Delivery Fee              : {int(delivery_fee):,} sum (Free Delivery: {free_delivery})")

print("\n--- FINAL TOTAL ---")
print(f"Final Amount to Pay       : {int(final_total):,} sum")
print(f"Total Amount Saved        : {int(total_saved):,} sum")
print("==================================")
