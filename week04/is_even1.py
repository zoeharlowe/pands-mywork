# is_even1.py
# This program is based on is_even.py 
# It will round the decimals before outputting the result

# I used the round() function to round the input number to the nearest whole number
raw_number = float(input("Please enter a number: "))
rounded_number = round(raw_number)

if rounded_number % 2 == 0:
    print(f"{rounded_number} is an even number")
else:
    print(f"{rounded_number} is an odd number")