# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders):
    
    if not orders:
        return 0
    
    valid_orders = [
        order for order in orders 
        if isinstance(order, dict) and order.get("status") != "cancelled"
    ]
    
    if not valid_orders:
        return 0
    
    total = sum(order.get("amount", 0) for order in valid_orders)
    
    return total / len(valid_orders)