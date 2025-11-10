# 팰린드롬?
import sys
input = sys.stdin.readline

# 길이가 N인 수열
N = int(input())
num_list = list(map(int, input().split()))

# DP 테이블 초기화
# 시간 초과 때문에 dp로 미리 계산
dp = [[0] * N for _ in range(N)]

for i in range(N):
    # 길이 1인 팰린드롬
    dp[i][i] = 1
    # 길이 2인 팰린드롬
    if i < N - 1 and num_list[i] == num_list[i + 1]:
        dp[i][i + 1] = 1

# 길이 3 이상인 팰린드롬
for length in range(3, N + 1):  # 부분 수열의 길이
    for start in range(N - length + 1): # 0 ~ N - length
        # 부분 수열의 끝 인덱스
        end = start + length - 1
        # 양 끝이 같고, 그 안쪽이 팰린드롬이면 팰린드롬
        if num_list[start] == num_list[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1

# M개의 질문
M = int(input())

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])