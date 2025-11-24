# 행렬 곱셈 순서
import sys
input = sys.stdin.readline

n = int(input())
# 행렬들을 담을 리스트
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

for length in range(1, n):
    for start in range(0, n - length):
        end = start + length
        # length가 1일 때
        if length == 1:
            dp[start][end] = matrix[start][0] * matrix[start][1] * matrix[end][1]
            continue
        # dp 테이블 채우기
        dp[start][end] = 2 ** 32
        for split in range(start, end):
            dp[start][end] = min(
                dp[start][end],
                dp[start][split] + dp[split + 1][end] 
                + matrix[start][0] * matrix[split][1] * matrix[end][1])
# dp테이블의 가장 오른쪽 위가 모든 행렬들의 곱셈을 하기 위한 곱셈의 수의 최솟값
print(dp[0][n - 1])