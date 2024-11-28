# Story: You have received an encrypted message where each character has been shifted forward by a fixed number in the alphabet. For example, if the shift is 2, 'a' becomes 'c', 'b' becomes 'd', and so on. You need to decrypt the message by shifting the characters back to their original positions.

# Problem: Write a Python program that takes an encrypted message and a shift value, then prints the decrypted message.

msg = input("Enter the message: ")
shift = int(input("Enter shift: "))
dc = ''
for char in msg:
    if char.isalpha():  
        start = ord('A') if char.isupper() else ord('a')
        new_char = chr((ord(char) - start - shift) % 26 + start)
        dc += new_char
    else:
        dc += char
print("Decrypted message:", dc)
