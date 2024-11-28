'''
Find the Missing Number in a Sequence
'''
n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1):
    if arr[i+1] - arr[i] != 1:
        print(arr[i+1]-1)