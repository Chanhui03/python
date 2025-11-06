# N-Queen

import sys
input = sys.stdin.readline
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[i] - row[x]) == abs(i - x):
            return False
    return True

def n_queen(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        row[x] = i
        if is_promising(x):
            n_queen(x + 1)
            
n_queen(0)
print(ans)