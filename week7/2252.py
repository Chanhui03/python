# 줄 세우기
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
que = deque()

result = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    tmp = que.popleft()
    result.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)

for i in result:
    print(i, end = " ")