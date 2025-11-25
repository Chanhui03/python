# 합이 0인 네 정수
import sys
input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
for a in A:
    for b in B:
        AB.append(a + b)
AB.sort()

CD = []
for c in C:
    for d in D:
        CD.append(c + d)
CD.sort()

result = 0
left, right = 0, len(CD) - 1

while (0 <= right) and (left < len(AB)):
    sum = AB[left] + CD[right]
    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    # 합이 0일 때 중복 값 처리 구간
    else:
        x = 1
        for i in range(left + 1, len(AB)):
            if AB[left] == AB[i]:
                x += 1
            else:
                break
        y = 1
        for i in range(right -1, -1, -1):
            if CD[right] == CD[i]:
                y += 1
            else:
                break
        # 중복 포함 result 증가
        result += x * y
        left += x
        right -= y

print(result)