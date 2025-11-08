# 평범한 배낭

import sys
input = sys.stdin.readline

# n = 물품의 수
# k = 버틸 수 있는 무게
n, k = map(int, input().split())

# 각 물건의 무게, 해당 물건의 가치 입력받기
bag = [list(map(int, input().split())) for _ in range(n)]

# dp 초기화
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        current_w, current_v = bag[i-1]
        if j >= current_w:
            dp[i][j] = max(bag[i - 1][1] + dp[i - 1][j - bag[i - 1][0]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])

#6 13
#