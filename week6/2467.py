# 용액

import sys
input = sys.stdin.readline

n = int(input())

liquids = list(map(int, input().split()))
liquids.sort()

left, right = 0, n - 1
best_sum = float('inf')
result = (0, 0)

while left < right:
    current_sum = liquids[left] + liquids[right]
    
    if abs(current_sum) < abs(best_sum):
        best_sum = current_sum
        result = (liquids[left], liquids[right])
        
    if current_sum < 0:
        left += 1
    else:
        right -= 1
print(result[0], result[1])