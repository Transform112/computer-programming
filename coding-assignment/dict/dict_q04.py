'''
Write a Python program to create and display all combinations of letters, selecting
each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
'''
data = {'1': ['a', 'b'], '2': ['c', 'd']}
lists = list(data.values())
for item1 in lists[0]:
    for item2 in lists[1]:
        print(item1 + item2)
