# Story: You are working at a name badge company, and you need to print out names in reverse order for a special event. The names are entered as "First Last", and you need to print them as "Last First".

# Problem: Write a Python program that takes a list of names in "First Last" format and prints them in "Last First" format.

st = input("Enter a string :")
li = st.split()
for i in range(1, len(li), 2):
    print(li[i], li[i-1], end=' ')