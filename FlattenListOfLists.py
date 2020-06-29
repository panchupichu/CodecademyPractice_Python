"""Make a function that flattens the list of lists
   https://www.codecademy.com/courses/learn-python/lessons/lists-and-functions/exercises/using-a-list-of-lists-in-a-function
   Python 3 debugged with Thonny
"""
#Sample list of lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists:
        for i in numbers:
            results.append(i)
    return results

print(flatten(n))
