# 트리의 지름

import sys
from collections import defaultdict, deque

def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor, weight in tree[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + weight
                queue.append(neighbor)
    
    farthest_node = visited.index(max(visited))
    max_distance = max(visited)
    return farthest_node, max_distance


input = sys.stdin.readline
n = int(input())

tree = defaultdict(list)
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

# 첫 번째 BFS로 임의의 노드에서 가장 먼 노드 찾기
farthest_node, _ = bfs(1)
# 두 번째 BFS로 그 노드에서 가장 먼 노드까지의 거리 찾기
_, diameter = bfs(farthest_node)
print(diameter)

