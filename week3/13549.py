# 숨바꼭질 3

import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
limit = 100001
cnt = [0] * limit

# 방문시간 기록 배열
visited = [False] * limit

def bfs(x, end):
    dq = deque()
    # 시작위치 x
    dq.append(x)

    # dq 반복
    while dq:
        x = dq.popleft()

        # 목표 위치 도달 시 종료
        if x == end:
            return cnt[x]
        # 우선 순위 x*2(0초) > x-1(1초) > x+1(1초)
        if -1 < x * 2 < limit and visited[x * 2] == 0:
            dq.appendleft(x * 2)
            cnt[x * 2] = cnt[x]
            visited[x * 2] = True
        if -1 < x - 1 < limit and visited[x - 1] == 0:
            dq.append(x - 1)
            cnt[x - 1] = cnt[x] + 1
            visited[x - 1] = True
        if -1 < x + 1 < limit and visited[x + 1] == 0:
            dq.append(x + 1)
            cnt[x + 1] = cnt[x] + 1
            visited[x + 1] = True

print(bfs(n, k))