'''
Find Pairs with Given Sum
'''
n = int(input())
n_arr = list(map(int, input().split()))
target_sum = int(input())
for i in n_arr:
    for j in range(1,i+1):
        if i + j == target_sum:
            print(i,j) 