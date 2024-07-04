# Prompt the user to input the number for which they want the multiplication table
n = int(input("What's the number for the multiplication table you want ? "))

# Inform the user of their choice
print(f"\nYou chose the multiplication table of {n} , here we go:")

# Create a range from 1 to 12 (inclusive) to use for multiplication
s = range(1, 13)

# Loop through the range and print the multiplication table for the chosen number
for i in s:
    print(f"{n} X {i} = {n * i}")