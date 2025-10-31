# Define a function calculate_delivery_revenue(order_type, deliveries_completed, time_period) that:
# For “express”: earns $8/delivery at morning period, $12 at lunch, $18 at dinner
# For “regular”: earns $5/delivery at morning period, $8 at lunch, $12 at dinner
# For “bulk”: earns $15/delivery at morning period, $22 at lunch, $30 at dinner
# Return the total delivery revenue
def calculate_delivery_revenue(order_type, deliveries_completed, time_period):
    if order_type == "express":
        if time_period == "morning":
            time_period = 8
        elif time_period == "lunch":
            time_period = 12
        elif time_period == "dinner":
            time_period = 18
    elif order_type == "regular":
        if time_period == "morning":
            time_period = 5
        elif time_period == "lunch":
            time_period = 8
        elif time_period == "dinner":
            time_period = 12
    elif order_type == "bulk":
        if time_period == "morning":
            time_period = 15
        elif time_period == "lunch":
            time_period = 22
        elif time_period == "dinner":
            time_period = 30
    else:
        return "wrong type of order"
    total = deliveries_completed * time_period
    return total
# Define a function calculate_completion_rate(driver_months, baseline_orders, completed_orders) that:
# Calculate expected orders: 1000 + (driver_months * 100)
# Calculate order capacity: expected_orders - baseline_orders
# Calculate completion percentage: (completed_orders - baseline_orders) / order_capacity * 100
# Return the completion percentage
def calculate_completion_rate(driver_months, baseline_orders, completed_orders):
    calculate_expected_orders = 1000 + (driver_months * 100)
    calculate_order_capacity = calculate_expected_orders - baseline_orders
    calculate_completion_percentage = (completed_orders - baseline_orders) / calculate_order_capacity * 100
    return calculate_completion_percentage
# Define a function determine_driver_tier(completion_percent) that:
# Below 50%: “Starter Tier”
# 50-60%: “Bronze Tier”
# 60-70%: “Silver Tier”
# 70-85%: “Gold Tier”
# Above 85%: “Elite Tier”
def determine_driver_tier(completion_percent):
    if completion_percent < 50:
        return "Starter Tier"
    elif completion_percent < 60:
        return "Bronze Tier"
    elif completion_percent < 70:
        return "Silver Tier"
    elif completion_percent < 85:
        return "Gold Tier"
    else:
        return "Elite Tier"
# Define a function calculate_total_earnings(revenue, deliveries, tier_bonus) that:
# Base earnings = revenue * 0.05 + deliveries * 2
# Tier bonuses: Starter=0.5, Bronze=1.0, Silver=1.2, Gold=1.5, Elite=1.8
# Return the final earnings rounded to 1 decimal place
def calculate_total_earnings(revenue, deliveries, tier_bonus):
    base_earnings = revenue * 0.05 + deliveries * 2
    if tier_bonus == "Starter Tier":
        tier_bonus = 0.5
    elif tier_bonus == "Bronze Tier":
        tier_bonus = 1.0
    elif tier_bonus == "Silver Tier":
        tier_bonus = 1.2
    elif tier_bonus == "Gold Tier":
        tier_bonus = 1.5
    elif tier_bonus == "Elite Tier":
        tier_bonus = 1.8
    final_earnings = base_earnings * tier_bonus
    return final_earnings
# Define a function needs_route_optimization(delivery_days, total_deliveries, avg_completion) that:
# Returns True if delivery_days >= 6 AND avg_completion < 50
# Returns True if total_deliveries < 100 AND avg_completion < 60
# Returns True if delivery_days >= 4 AND avg_completion < 40
# Otherwise returns False
def needs_route_optimization(delivery_days, total_deliveries, avg_completion):
    if delivery_days >= 6 and avg_completion < 50:
        return "Yes"
    elif total_deliveries < 100 and avg_completion < 60:
        return "Yes"
    elif delivery_days >= 4 and avg_completion < 40:
        return "Yes"
    else:
        return "No"
# Define a function generate_delivery_summary(driver_name, order_type, deliveries, time_period, driver_months, baseline_orders, completed_orders, delivery_days) that:
# Calls all necessary functions to calculate metrics
# Prints a formatted summary (no return value)
# Include all calculated values and recommendations
# Testing Inputs: Test your system with these delivery records:
print('FOOD DELIVERY PERFORMANCE TRACKER')
def generate_delivery_summary(driver_name, order_type, deliveries, time_period, driver_months, baseline_orders, completed_orders, delivery_days):
    revenue=calculate_delivery_revenue(order_type, deliveries, time_period)
    completion_percent=calculate_completion_rate(driver_months, baseline_orders, completed_orders)
    tier_bonus=determine_driver_tier(completion_percent)
    total_earnings=calculate_total_earnings(revenue, deliveries, tier_bonus)
    needs_optimization=needs_route_optimization(delivery_days, deliveries, completed_orders)
   
    
    print('========================================')
    print(f'Delivery Summary for: {driver_name}')
    print('----------------------------------------')
    print(f'Order type: {order_type}')
    print(f'Deliveries Completed: {deliveries}')
    print(f'Time Period: {time_period}')
    print(f'Delivery Revenue: ${revenue}')
    print('Completion Analysis:')
    print(f'  Experience: {driver_months} months, Baseline: {baseline_orders}, Completed Orders: {completed_orders}')
    print(f'  Completion Rate: {completion_percent:.1f}%')
    print(f'  Driver Tier: {tier_bonus}')
    print(f'Total Earnings: {total_earnings:.1f}')
    print(f'Delivery Days: {delivery_days}')
    print(f'Route Optimization Needed: {needs_optimization}')
    print()
    
    
# Record 1: “Drew”, “bulk”, 45 deliveries, “dinner”, driver_months=3, baseline_orders=800, completed_orders=1150, delivery_days=3
# Record 2: “Ellis”, “regular”, 60 deliveries, “lunch”, driver_months=5, baseline_orders=900, completed_orders=1300, delivery_days=5
# Record 3: “Frankie”, “express”, 30 deliveries, “morning”, driver_months=8, baseline_orders=850, completed_orders=950, delivery_days=7
# Expected Output
generate_delivery_summary('Drew', 'bulk', 45, 'dinner', 3, 800, 1150, 3)
generate_delivery_summary('Ellis', 'regular', 60, 'lunch', 5, 900, 1300, 5)
generate_delivery_summary('Frankie', 'express', 30, 'morning', 8, 850, 950, 7)
# FOOD DELIVERY PERFORMANCE TRACKER
# ========================================
# Delivery Summary for: Drew
# ----------------------------------------
# Order Type: bulk
# Deliveries Completed: 45
# Time Period: dinner
# Delivery Revenue: $1350
# Completion Analysis:
#   Experience: 3 months, Baseline: 800, Completed Orders: 1150
#   Completion Rate: 70.0%
#   Driver Tier: Gold Tier
# Total Earnings: $236.2
# Delivery Days: 3
# Route Optimization Needed: No

# ========================================
# Delivery Summary for: Ellis
# ----------------------------------------
# Order Type: regular
# Deliveries Completed: 60
# Time Period: lunch
# Delivery Revenue: $480
# Completion Analysis:
#   Experience: 5 months, Baseline: 900, Completed Orders: 1300
#   Completion Rate: 66.7%
#   Driver Tier: Silver Tier
# Total Earnings: $172.8
# Delivery Days: 5
# Route Optimization Needed: No

# ========================================
# Delivery Summary for: Frankie
# ----------------------------------------
# Order Type: express
# Deliveries Completed: 30
# Time Period: morning
# Delivery Revenue: $240
# Completion Analysis:
#   Experience: 8 months, Baseline: 850, Completed Orders: 950
#   Completion Rate: 10.5%
#   Driver Tier: Starter Tier
# Total Earnings: $36.0
# Delivery Days: 7
# Route Optimization Needed: Yes