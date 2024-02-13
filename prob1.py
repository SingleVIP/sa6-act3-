"""
Problem 1: Sum of Digits
Objective: Write a Python program that uses a lambda function to compute the 
sum of the digits of a given number.
Hint: You may need to convert the number to a string to iterate over 
its digits, then back to integers to sum them.
"""
sum_of_digits = lambda n: sum(int(digit) for digit in str(n) if digit.isdigit())
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("The sum of digits of the number", num, "is:", result)
