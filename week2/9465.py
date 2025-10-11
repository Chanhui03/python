# 스티커

import sys

testCase = int(sys.stdin.readline())
for _ in range(testCase):
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + arr[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))