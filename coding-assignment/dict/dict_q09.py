'''
Write a Python program to sort Counter by value.
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
'''
data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
items = list(data.items())
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1]:
            items[i], items[j] = items[j], items[i]
print(items)
