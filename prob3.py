"""
Problem 3: Find Maximum
Objective: Implement a function that takes a list of numbers and a lambda function 
as arguments. The lambda function should compare two numbers and return the greater 
of the two. Use this lambda function to find the maximum number in the list without 
using the built-in max() function.
Hint: Initialize your maximum with the first element of the list and then iterate 
over the list, using the lambda function to update the maximum.
"""
def find_maximum(numbers, compare):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if compare(num, max_num) > 0:
            max_num = num
    return max_num
greater = lambda x, y: x if x > y else y
numbers_list = [10, 25, 8, 37, 42, 15]
maximum_number = find_maximum(numbers_list, greater)
print("Maximum number in the list:", maximum_number)