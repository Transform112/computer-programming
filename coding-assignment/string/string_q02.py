# Problem: Write a function to check if a given string is a palindrome.

# Scenario: You need to verify if a user-entered string reads the same forward and backward.

st = input("Enter a string :")
rev_st = st[::-1]
if st == rev_st:
    print("Yes")
else:
    print("No")