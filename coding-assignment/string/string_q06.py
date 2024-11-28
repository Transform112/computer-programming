# Problem (cont'd): Write a program that takes a list of names, rearranges them so that names starting with a vowel come first, and then prints the rearranged list.

names = input("Enter the names :").split()
vowels = 'AEIOUaeiou'
vowel_names = [name for name in names if name[0] in vowels]
other = [name for name in names if name[0] not in vowels]
final = vowel_names + other
result = ' '.join(final)
print(result)