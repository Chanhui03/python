# ACM Craft
from collections import deque
import sys

input = sys.stdin.readline


T = int(input())
result = []

for _ in range(T):
    # 건물의 수, 간선의 개수
    N, K = map(int, input().split())
    # 각 건물을 짓는데 걸리는 시간
    D = [0] + list(map(int, input().split()))
    # 간선 등록할 그래프
    graph = [[] for _ in range(N + 1)]
    # 진입 차수만 필요함
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)

    # 간선 입력받기
    for _ in range(K):
        X, Y = map(int, input().split())
        # 방향 그래프
        graph[X].append(Y)
        indegree[Y] += 1
    
    # 위상정렬 알고리즘에 쓸 큐 생성
    que = deque()
    # 초기에 진입차수가 0인 애들을 큐에 넣어둠 + dp에도 넣음
    for i in range(1, N + 1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = D[i]
    
    while que:
        tmp = que.popleft()
        for i in graph[tmp]:
            indegree[i] -= 1
            dp[i] = max(dp[tmp] + D[i], dp[i])
            if indegree[i] == 0:
                que.append(i)
    
    W = int(input())
    result.append(dp[W])

for i in result:
    print(i)