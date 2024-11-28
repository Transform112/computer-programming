# Problem: Write a function to count the number of vowels in a string.

# Scenario: You are tasked with calculating how many vowels appear in a given sentence.

st = input("Enter a string :").lower()
vowels = 'aeiou'
count = 0
for i in st:
    if i in vowels:
        count += 1
print(count)