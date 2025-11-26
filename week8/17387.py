import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

point_1 = [x1, y1]
point_2 = [x2, y2]
point_3 = [x3, y3]
point_4 = [x4, y4]

# ccw 값 +1 (반시계), 0 (일직선), -1 (시계)
def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    temp1 = (x1 * y2) + (x2 * y3) + (x3 * y1)
    temp2 = (x3 * y2) + (x2 * y1) + (x1 * y3)

    result = temp1 - temp2

    if result > 0:
        return 1
    if result == 0:
        return 0
    return -1

# 선분 교차 판정 함수
def cross_check(p1, p2, p3, p4):
    # CCW 방향 비교
    # line1과 p3 비교
    ccw1 = ccw(p1, p2, p3)
    # line1과 p4 비교
    ccw2 = ccw(p1, p2, p4)

    # line2와 p1 비교
    ccw3 = ccw(p3, p4, p1)
    # line2와 p2 비교
    ccw4 = ccw(p3, p4, p2)

    # 네 점이 일직선
    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        if (min(p1[0], p2[0]) <= max(p3[0], p4[0]) and
            min(p3[0], p4[0]) <= max(p1[0], p2[0]) and
            min(p1[1], p2[1]) <= max(p3[1], p4[1]) and
            min(p3[1], p4[1]) <= max(p1[1], p2[1])):
            return 1
        else:
            return 0

    # 일반적인 교차 조건
    if (ccw1 * ccw2 <= 0) and (ccw3 * ccw4 <= 0):
        return 1
    return 0

print(cross_check(point_1, point_2, point_3, point_4))
