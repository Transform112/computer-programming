'''
Find the Second Largest Element in an Array
'''
number_element = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[-2])
           