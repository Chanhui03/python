# 음악프로그램
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# 밑에 두 줄은 거의 고정인 듯
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

result = []
que = deque()

for _ in range(m):
    pd_list = list(map(int, input().split()))
    # 0번째 무시, 마지막 무시
    for i in range(1, len(pd_list) - 1):
        graph[pd_list[i]].append(pd_list[i + 1])
        indegree[pd_list[i + 1]] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    tmp = que.popleft()
    result.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)

if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)