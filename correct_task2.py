# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    if not emails:
        return 0
    
    count = 0
    for email in emails:
        if not isinstance(email, str):
            continue
        
        if "@" not in email or email.count("@") != 1:
            continue
                
        parts = email.split("@")
        if parts[0] and parts[1] and "." in parts[1]:
            count += 1
    
    return count