# Problem 2:
# Find whether the given number ends with 0 or 5 or any other number.

# Function to check if number ends with 0 or 5
def check_last_digit(num):
    # Take the absolute value to ignore the negative sign
    last_digit = abs(num) % 10

    # If the last digit is 0
    if last_digit == 0:
        return "0"
    # If the last digit is 5
    elif last_digit == 5:
        return "5"
    # If the last digit is something else
    else:
        return "Other"

# Test Cases Table (from the problem image)
test_cases = [
    # Sr. No.  Input   Expected Output
    (1, 20, "0"),      # Ends with 0
    (2, 14, "Other"),  # Ends with 4
    (3, 5, "5"),       # Ends with 5
    (4, 0, "0"),       # Zero itself
    (5, -27, "Other"), # Ends with 7 (ignore negative)
    (6, -10, "0"),     # Ends with 0 (ignore negative)
]

# Test the function with all test cases
for sr_no, value, expected in test_cases:
    result = check_last_digit(value)
    print(f"Test Case {sr_no}: Input = {value}, Expected = {expected}, Got = {result}, Status = {'✅' if result == expected else '❌'}")
