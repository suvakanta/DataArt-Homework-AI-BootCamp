import re

def extract_calibration_value(line):
    # Find all digits in the line
    digits = re.findall(r'\d', line)
    
    # If there are at least two digits, use the first and last
    if len(digits) >= 2:
        first_digit = digits[0]
        last_digit = digits[-1]
        # Combine them as a two-digit number
        return int(first_digit + last_digit)
    else:
        # If no valid digits, return 0
        return 0

def sum_calibration_values(calibration_document):
    total_sum = 0
    for line in calibration_document:
        total_sum += extract_calibration_value(line)
    return total_sum

# Example input
calibration_document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

# Calculate the total sum of calibration values
total_calibration_sum = sum_calibration_values(calibration_document)
print("Total Calibration Sum:", total_calibration_sum)
