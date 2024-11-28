# Story: In a cybersecurity class, you are learning about strong passwords. Your teacher has given you a list of passwords and asked you to determine which passwords are "strong". A strong password is defined as one that has at least 8 characters, contains both uppercase and lowercase letters, and has at least one number.

# Problem: Write a Python program that reads a list of passwords and prints "strong" if the password is strong, otherwise "weak".

password = input("Enter the passwords :").split()
numb = '1234567890'
ls = []
for i in password:
    upper = 0
    lower = 0
    num = 0
    
    for j in i:
        if j.isupper():
            upper += 1
        if j.islower():
            lower += 1
        if j in numb:
            num += 1
    if len(i) >= 8 and upper >= 1 and lower >= 1 and num >= 1:
        ls.append("strong")
    else:
        ls.append("weak")
print(' '.join(ls))