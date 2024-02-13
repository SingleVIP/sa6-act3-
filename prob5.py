"""
Problem 5: Exponential Mapping
Objective: Given a list of numbers and a constant value n, use a lambda function with 
map() to raise each number in the list to the power of n.
Hint: The lambda function should take one argument and use the constant n within 
its expression to compute the power.
"""
numbers = [1, 2, 3, 4, 5]
n = 3
result = list(map(lambda x: x ** n, numbers))
print("List after raising each number to the power of", n, ":", result)