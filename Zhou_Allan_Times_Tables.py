# Times Tables
# Generates a multiplication table from two integers, given by the user. 
# The maximum number of rows is 20 and the maximum number of columns is
# 15. 

print("TIMES TABLE\n")

MAX_ROWS = 20 
MAX_COLUMNS = 15
PADDING = 5  # Spacing around each number of the times table.

# Ensure that the user enters an integer. Keep asking for input until 
# user enters integer. 
while True: 
    try: 
        rows = int(input("Enter the number of rows (maximum is 20): "))
        columns = int(input("Enter the number of columns (maximum is 15): "))

        # Check if numbers are within dimension boundaries (maximum 20 rows, 
        # 15 columns). If within boundaries, the while loop will be exited.
        if rows > MAX_ROWS and columns > MAX_COLUMNS: 
            print("Please lower the number of rows and columns.\n") 

        elif rows > MAX_ROWS:
            print("Please lower the number of rows.\n") 

        elif columns > MAX_COLUMNS:
            print("Please lower the number of columns.\n")

        else: 
            break 

    except ValueError: 
        print("Not an integer! Try again. \n")

print() 

# Each column has a width of 5. These spaces align the row of dashes
# with the columns of numbers. 
print(" " * PADDING, end = '') 

# Print the numbers 1 to columns, including columns itself. 
for i in range(1, columns + 1): 
    print("{:{width}}".format(i, width = PADDING), end = '')

# Print 5 dashes per number on the line below, since each column 
# has a width of 5. 
print("\n" + " " * PADDING + "-" * PADDING * columns) 

# Print the row number and all the multiples up to the nth multiple,
# where n is the column number, all with a spacing of 5. "i" represents
# the row number and "j" represents the column number.
for i in range(1, rows + 1): 
    # Use width = PADDING - 2, since there is a " |" after the row number. 
    print("{:{width}} |".format(i, width = PADDING - 2), end = '')

    # The number being printed will be row number x column number. 
    for j in range(1, columns + 1):
        print("{:{width}}".format(i * j, width = PADDING), end = '')

    print() # Move to next row of numbers.

print()