# Story: Your friend has sent you a long email where none of the sentences start with a capital letter. To make the email look nicer, you want to capitalize the first letter of each sentence.

# Problem: Write a Python program that takes a paragraph of text and capitalizes the first letter of each sentence.

para = input("Enter a paragraph :").split('. ')
l = []
for i in para:
    c = i[0].upper() + i[1:]
    l.append(c)
print('. '.join(l))
