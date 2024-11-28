'''
Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item':
'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
'''
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = {}
for entry in data:
    item = entry['item']
    amount = entry['amount']
    if item in result:
        result[item] += amount
    else:
        result[item] = amount
print(result)