# 호텔

import sys
input = sys.stdin.readline

c, n = map(int, input().split())
cost_list = [list(map(int, input().split())) for _ in range(n)]

# c + 101은 100명의 고객을 추가로 받을 수 있는 여유 공간 확보
dp = [float('inf')] * (c + 101)
dp[0] = 0

for cost, customer in cost_list:
    for j in range(customer, c + 101):
        dp[j] = min(dp[j], dp[j - customer] + cost)

# c 이상 중 가장 작은 비용 출력
print(min(dp[c:]))