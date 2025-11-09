# 부분합

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

# 두 포인터 모두 0에서 시작
left, right = 0, 0

# 현재 부분합 초기화
current_sum = 0

# 최단 부분합 길이
min_length = float('inf')

while True:
    # 부분합이 s 이상일 때까지 right 포인터를 이동
    # 부분합이 s 이상이면 left 포인터를 이동하여 길이를 줄여봄
    if current_sum >= s:
        # 현재 부분합의 길이를 갱신
        min_length = min(min_length, right - left)
        current_sum -= numbers[left]
        left += 1
    # right 포인터가 배열 끝에 도달했으면 종료
    elif right == n:
        break
    # 부분합이 s 미만일 때 right 포인터 이동
    else:
        # 부분합에 right 위치의 수 더하기
        current_sum += numbers[right]
        right += 1

# min_length가 초깃값이면 부분합이 존재하지 않는 것
if min_length == float('inf'):
    print(0)
else:
    print(min_length)