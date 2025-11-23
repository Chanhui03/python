# 세 용액
import sys
input = sys.stdin.readline

N = int(input())
# 용액 특성값들 정렬해서 입력받기
list = sorted(list(map(int, input().split())))

# 임의의 max값
result = 4000000000
# 해답 용액 3개
solve = []

for i in range(N - 2):
    refer = list[i]
    left_pointer = i + 1
    right_pointer = N - 1
    while left_pointer < right_pointer:
        current_sum = refer + list[left_pointer] + list[right_pointer]
        if abs(current_sum) <= abs(result):
            solve = [refer, list[left_pointer], list[right_pointer]]
            result = refer + list[left_pointer] + list[right_pointer]
        if current_sum < 0:
            left_pointer += 1
        elif current_sum > 0:
            right_pointer -= 1
        else:
            break

for i in solve:
    print(i, end = " ")