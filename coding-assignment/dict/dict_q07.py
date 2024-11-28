'''
Write a Python program to replace dictionary values with their sum.
'''
data = [{'a': 100, 'b': 200}, {'a': 300, 'b': 100}, {'a': 50, 'c': 400}]
sum_dict = {}
for entry in data:
    for key, value in entry.items():
        if key in sum_dict:
            sum_dict[key] += value
        else:
            sum_dict[key] = value
print(sum_dict)
