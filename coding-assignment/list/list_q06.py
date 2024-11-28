'''
Find the Intersection of Two Arrays
'''
n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
intersection_mn = []
for i in arr_n:
    if i in arr_m:
        intersection_mn.append(i)
print(*intersection_mn)