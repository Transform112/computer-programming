'''
 Check if Array is a Subset of Another
'''
n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
count = 0
for i in arr_m:
    if i in arr_n:
        count += 1
if count == m:
    print("Yes")
else:
    print("No")      