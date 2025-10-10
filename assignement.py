# 1st function: Using Python built-in functions

# Input 
def built_in_functions_max(num1, num2, num3):
    print()
    print("=== Find the largest number among three numbers ===")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

# Output 
    largest = max(num1, num2, num3)
    print("The largest number is", largest)
    return largest
built_in_functions_max(0, 0, 0)



# 2nd function: Using Python built-in functions

# Input
def built_in_functions_min(numb1, numb2, numb3):
    print()
    print("=== Find the smallest number among three numbers ===")
    numb1 = int(input("Enter first number: "))
    numb2 = int(input("Enter second number: "))
    numb3 = int(input("Enter third number: "))

# Output
    minimum = min(numb1, numb2, numb3)
    print("The smallest number is", minimum)
    return minimum
built_in_functions_min(0, 0, 0)



# 3rd function: Conditional Statements - The If Statement

# Input 
def built_in_functions_positive_negative(x):
    print()
    print("=== Check if a number is positive, negative, or zero ===")
    x = int(input("Enter a number: "))

# Output 
    if x > 0:
        print(f"The number {x} is positive")
    elif x < 0:
        print(f"The number {x} is negative")
    else:
        print("The number is equal to zero")
        return x
built_in_functions_positive_negative(0)



# 4th function: For Loop - Making a Star Shape

# Input
def built_in_functions_star_shape(number):
    print()
    print("=== Display a star shape based on the number of rows ===")
    number = int(input("Enter a number: "))

# Output
    for i in range(number):
        print("*" * (i + 1))
built_in_functions_star_shape(0)



# 5th function: While Loop - Counting Multiples of 3

# Input
def built_in_functions_count_multiples_of_3(limit):
    print()
    print("=== Count from 1 to limit, replacing multiples of 3 with 'Multiple of 3' ===")
    limit = int(input("Enter the limit: "))

# Output 
    i = 1
    while i <= limit:
        if i % 3 == 0:
            print("Multiple of 3")
        else:
            print(i)
        i += 1
built_in_functions_count_multiples_of_3(0)



# 6th function: Sum of Even Numbers in a Range:

# Input 
def built_in_functions_sum_of_even_numbers(a, b):
    print()
    print("=== Calculate the sum of even numbers between two given numbers (inclusive) ===")  
    a = int(input("Enter the starting number: "))
    b = int(input("Enter the ending number: "))
    total = 0

# Output 
    for i in range(a, b +1):
        if i % 2 == 0:
            total += i
    print(f"The sum of even numbers between {a} and {b} is {total}")
    return total
built_in_functions_sum_of_even_numbers(0, 0)
