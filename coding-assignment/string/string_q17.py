# Story: You are reading a large book, and you want to find out which words are repeated the most. Your task is to write a Python program that takes a paragraph of text and prints the most frequent word(s).

# Problem: Write a Python program that reads a paragraph and prints the word that appears the most frequently.

st = input().split()
word = ''
count = 0

for i in st:
    if st.count(i) > count:
        count = st.count(i)
        word = i
print(word)