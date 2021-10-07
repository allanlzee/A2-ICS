# Times Tables
# Generates a multiplication table from two positive integers, 
# given by the user. The maximum number of rows is 20 and the
# maximum number of columns is 15. 
# Author: Allan Zhou 

print("TIMES TABLE\n")

MAX_ROWS = 20 
MAX_COLUMNS = 15

# Spacing around each number of the times table.
PADDING = 5

# Ensure that the user enters valid input (positive integer).
while True: 
    try: 
        rows = int(input("Enter the number of rows (1 to 20): "))
        
        # Check if rows is within the maximum boundary of 20 rows.
        if rows > MAX_ROWS:
            print("Please lower the number of rows.\n") 
            continue

        # Rows cannot be negative integers.
        elif rows <= 0: 
            print("Please input a positive integer for rows.\n")
            continue

        columns = int(input("Enter the number of columns (0, 15): "))

        # Check if columns is within the maximum boundary of 15 columns.
        if columns > MAX_COLUMNS:
            print("Please lower the number of columns.\n")
            continue
        
        # Columns cannot be negative integers. 
        elif columns <= 0: 
            print("Please input a positive integer for columns.\n")
            continue
        
        break

    # Catch invalid inputs to keep the program from crashing. 
    except ValueError:  
        print("Not an integer! Try again.\n")

print("\nMultiplication Table of {} by {}.\n".format(rows, columns)) 

# Each column has a width of 'PADDING'. The first column has will be 
# spaces only for alignment. 
print(" "*PADDING, end='') 

# Print the numbers 1 to columns, including columns itself. 
for i in range(1, columns + 1): 
    print("{:{width}}".format(i, width=PADDING), end='')

# Print dashes for each column (of width 'PADDING') on the line below. 
# The first column has no dashes, so print spaces. 
print("\n" + " "*PADDING + "-"*PADDING*columns) 
 
# "i" represents the row number and "j" represents the column number.
for i in range(1, rows + 1): 

    # Use width = PADDING - 2, since there is " |" (2 characters) 
    # after the row number. 
    print("{:{width}} |".format(i, width=PADDING-2), end='')

    # Print the multiples up to the nth multiple, where n is the
    # column number, all with spacing of 'PADDING'.
    for j in range(1, columns + 1):
        print("{:{width}}".format(i * j, width=PADDING), end='')

    print() 

print()
