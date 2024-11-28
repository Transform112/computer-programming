# Story: The town market is having a sale, and the shopkeeper wants to display the price tags in reverse order for some reason. The prices of the items are written in a single line, and you are tasked with reversing the digits of each price individually.

# Problem: Write a Python program that reads a list of prices, reverses the digits of each price, and prints the reversed prices.

prices = input("Enter the prices :").split()
ls = []
for i in range(len(prices)):
    m = prices[i]
    ls.append(m[::-1])
result = ' '.join(ls)
print(result)