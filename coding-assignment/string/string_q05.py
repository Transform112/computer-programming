# Problem: Write a function to check if two strings are anagrams (i.e., they contain the same characters in different order).

# Scenario: You are working on a text processing tool and need to check if two words are anagrams.

st1 = input("Enter a word :")
st2 = input("Enter a word :")

if sorted(st1) == sorted(st2):
    print("Yes")
else:
    print("No")