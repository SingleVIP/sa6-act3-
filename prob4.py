"""
Problem 4: Intersection of Two Lists
Objective: Write a Python program that finds the intersection of two lists using a 
lambda function and the filter() function. The program should return a list of 
elements that are present in both lists.
Hint: You may want to use the filter() function to keep only the elements in one 
list that are also contained in the other list.
"""
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list(filter(lambda x: x in list1, list2))
print("Intersection of the two lists:", intersection)