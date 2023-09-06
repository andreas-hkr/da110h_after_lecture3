message = "Hello, World!"   # Text/string
number = 42                 # Integer
balance = 123.45            # Float

# Use a minimum width of 20 characters
print(f'{message:20}')      # Text/strings are left-aligned by default
print(f'{number:20}')       # Numbers are right-aligned by default
print(f'{balance:20}')

# Use a minimum width of 20 characters, and align the output
print(f'{message:>20}')     # Right-aligned
print(f'{number:<20}')      # Left-aligned
print(f'{balance:^20}')     # Center-aligned

# Use 2 decimal places
# print(f'{number:.2}')     # This is invalid as Python knows number as an integer and can not print decimals
print(f'{number:.2f}')      # This is valid as Python now knows number as a float
print(f'{balance:.2}')      # Without the 'f' Python will use default for floats (this is 'g' instead of 'f')
print(f'{balance:.2f}')     # This is valid as Python knows balance is a float

# Use a minimum width of 20 characters, align the output, and use 2 decimal places
print(f'{number:<20.2f}')   # Left-aligned
print(f'{balance:^20.2f}')  # Center-aligned
