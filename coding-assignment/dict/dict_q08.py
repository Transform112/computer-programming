'''
Write a Python program to create a dictionary from two lists without losing duplicate
values.
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII':
{3}, 'Class-V': {1}})
'''
list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]
result = {}
for i in range(len(list1)):
    if list1[i] in result:
        result[list1[i]].add(list2[i])
    else:
        result[list1[i]] = {list2[i]}
print(result)
