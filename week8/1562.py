# 계단 수
import sys
input = sys.stdin.readline

# 10억으로 나눈 나머지 출력
MOD = 1000000000

n = int(input())

# dp[length][last_digit][mask]
dp = [[[0] * 1024 for _ in range(10)] for _ in range(n + 1)]

# dp 테이블 초깃값 설정
# 길이가 1인 계단 수는 1 ~ 9로 시작해야함 (0은 불가능)
for digit in range(1, 10):
    dp[1][digit][1 << digit] = 1

# length = n일 때 가능한 length = n + 1 채우기
for length in range(1, n):
    for last_digit in range(0, 10):
        for mask in range(1024):
            # length가 1일 때 초기화 하지 않은 값들은 모두 0이라서 건너뜀
            if dp[length][last_digit][mask] == 0:
                continue
            
            # 다음 숫자들은 last-1, last+1
            for nxt in [last_digit - 1, last_digit + 1]:
                # 다음 숫자가 0 ~ 9에 포함되면 실행
                if 0 <= nxt <= 9:
                    # new_mask는 현재 mask에 nxt 비트 OR 연산
                    new_mask = mask | (1 << nxt)
                    # 다음 상태 dp[length + 1]에 현재 상태 누적 
                    dp[length + 1][nxt][new_mask] += dp[length][last_digit][mask]
                    dp[length + 1][nxt][new_mask] %= MOD

full_mask = (1 << 10) - 1
ans = 0

for d in range(10):
    # full_mask인 것만 ans에 추가
    ans = (ans + dp[n][d][full_mask]) % MOD

print(ans)
