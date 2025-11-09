# LCS 2
import sys
input = sys.stdin.readline

# 첫번째 입력
str_1 = input().rstrip()
# 두번째 입력
str_2 = input().rstrip()

len1 = len(str_1)
len2 = len(str_2)

# DP 테이블 초기화 (LCS 길이 저장)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

# DP 테이블 채우기
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str_1[i - 1] == str_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 길이 출력
print(dp[len1][len2])

# 역추적 (backtracking)으로 LCS 문자열 구하기
if dp[len1][len2] != 0:
    i, j = len1, len2
    lcs_chars = []

    while i > 0 and j > 0:
        # 문자가 같으면 LCS에 포함되는 문자
        current_char_1 = str_1[i - 1]
        current_char_2 = str_2[j - 1]
        if current_char_1 == current_char_2:
            lcs_chars.append(current_char_1)
            i -= 1
            j -= 1
        else:
            # dp[i-1][j] = 위쪽, dp[i][j-1] = 왼쪽
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    # 거꾸로 채웠으니 뒤집어서 출력
    lcs_chars.reverse()
    print(''.join(lcs_chars))
