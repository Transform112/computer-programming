'''
Write a Python program to print a dictionary in table format
'''
data = {'Name': 'Alice', 'Age': 25, 'Country': 'USA', 'Profession': 'Engineer'}
print(f"{'Key':<15} {'Value':<15}")
print('-' * 30)
for key, value in data.items():
    print(f"{key:<15} {value:<15}")
