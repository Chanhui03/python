# 파티

import sys
input = sys.stdin.readline

import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)

def dijkstra(start):
    distances = [INF] * (n + 1)
    distances[start] = 0
    queue = [(0, start)]  # (거리, 노드)

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# x에서 각 노드까지의 최단 거리
dist_from_x = dijkstra(x)
max_round_trip = 0
for i in range(1, n + 1):
    dist_to_x = dijkstra(i)
    round_trip = dist_to_x[x] + dist_from_x[i]
    max_round_trip = max(max_round_trip, round_trip)

print(max_round_trip)