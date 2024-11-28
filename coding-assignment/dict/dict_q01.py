'''
Write a Python program to count the values associated with key in a dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name':
'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
'''

data = [
    {'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': True, 'name': 'Alex'}
]
count = 0
for entry in data:
    if entry['success'] == True:  
        count += 1  
print("Count of dictionaries with success as True:", count)
