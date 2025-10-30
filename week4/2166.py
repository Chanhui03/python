# 다각형의 면적

import sys
input = sys.stdin.readline

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

area = 0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    area += (x1 * y2) - (x2 * y1)

print(f"{abs(area) / 2:.1f}")