# Story: You are helping a railway station allocate seats to passengers. The station needs to seat people whose names start with a vowel in the front row and others in the back row. Your task is to rearrange the list of passengers accordingly.

# Problem: Write a program that takes a list of passenger names and arranges those whose names start with a vowel in the front, followed by the rest.


names = input("Enter the names :").split()
vowels = 'AEIOUaeiou'
vowel_names = [name for name in names if name[0] in vowels]
other = [name for name in names if name[0] not in vowels]
final = vowel_names + other
result = ' '.join(final)
print(result)