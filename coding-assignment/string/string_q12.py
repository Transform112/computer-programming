# Story: You are planning a trip and want to create an itinerary. You have a list of destinations, but they are all jumbled up. You want to print the destinations in alphabetical order so you can plan your trip better.

# Problem: Write a Python program that takes a list of destinations and prints them in alphabetical order.

st = input("Enter the string :").split()
l = sorted(st)
print(' '.join(l))