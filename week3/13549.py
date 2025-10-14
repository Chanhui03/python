# 숨바꼭질 3

import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
limit = 100001
cnt = [0] * limit
visited = [False] * limit

def bfs(x, end):
    dq = deque()
    dq.append(x)

    while dq:
        x = dq.popleft()
        if x == end:
            return cnt[x]
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