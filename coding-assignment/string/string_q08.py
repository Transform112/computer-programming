# Story: In a small village, there are many people with the same names. You have a list of names of people in the village, and your task is to remove the duplicates and print only the unique names.

# Problem: Write a Python program that takes a list of names and removes any duplicates, then prints the unique names.

names = input("Enter the names :").split()
ls = []
for i in names:
    if i not in ls:
        ls.append(i)
print(' '.join(ls))