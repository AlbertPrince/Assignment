# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    if not values:
        return 0
    
    total = 0
    count = 0
    
    for v in values:
        if v is not None:
            try:
                numeric_value = float(v)
                total += numeric_value
                count += 1
            except (ValueError, TypeError):
                continue
    
    return total / count if count > 0 else 0
