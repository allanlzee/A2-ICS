# Quadratic Solver
# Solves for the roots of the standard quadratic equation, ax² + bx + c = 0    
# using the quadratic formula ((-b ± √(b² - 4ac)) / (2a)) to solve for the
# roots (rounded to 2 decimal places) and the discriminant to determine the 
# number of real roots.
# Author: Allan Zhou 

from math import sqrt 

print("QUADRATIC SOLVER\n")

run = "y"

while run == "y" or run == "yes": 
    print("Enter the values of a, b, and c from a quadratic equation", \
    "ax² + bx + c = 0:")

    # Assume the user enters a valid input (float).
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print()

    # Calculate the discriminant using b² - 4ac. 
    discriminant = b**2 - 4*a*c 

    if discriminant > 0: 
        print("There are two solutions.")

        # The quadratic formula with a discriminant greater than 0 has two 
        # distinct roots: -b + √(b² - 4ac) / (2a) and -b - √(b² - 4ac) / (2a)
        first_root = (-b + sqrt(discriminant)) / (2 * a)
        second_root = (-b - sqrt(discriminant)) / (2 * a)

        print("The roots are {:.2f} and {:.2f}."
            .format(first_root, second_root))

    elif discriminant == 0: 
        print("There is one solution.")

        # The quadratic formula with a discriminant of 0 returns one root, 
        # -b / (2a), since the square root of 0 is 0. 
        first_root = -b / (2 * a) 
        print("The root is {:.2f}.".format(first_root))

    else: 
        # When the discriminant is negative, we get imaginary roots, 
        # which returns a math domain error in Python. 
        print("There are no (real) solutions.")

    # "yes" or "y" keeps the program running, anything else ends the program.
    run = input("\nAnother? (y)es or (n)o: ")

print("\nThanks for using QUADRATIC SOLVER.\nGood-bye!\n")
