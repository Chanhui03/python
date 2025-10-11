# LCS
# Longest Common Subsequence (최장 공통 부분 수열)
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제

import sys
input = sys.stdin.readline

str_1 = ' ' + input().rstrip()
str_2 = ' ' + input().rstrip()

# 일단 0으로 채우기 ?
dp = [[0] * len(str_2) for _ in range(len(str_1))]

for i in range(1, len(str_1)):
    for j in range(1, len(str_2)):
        if str_1[i] == str_2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])