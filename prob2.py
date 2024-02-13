"""
Problem 2: Custom Sort Order
Objective: Given a list of strings, use a lambda function to sort the list in 
ascending order based on the length of the strings. In case of a tie, sort 
the strings alphabetically.
Hint: The sorted() function's key parameter can take a lambda function that 
returns a tuple indicating the primary and secondary sort keys.
"""
strings_list = ["Peter", "Aaron", "Bob", "Jeff", "Jackson", "Nick"]
sorted_list = sorted(strings_list, key=lambda x: (len(x), x))
print("Sorted list:", sorted_list)