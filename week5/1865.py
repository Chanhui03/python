import sys
input = sys.stdin.readline

TC = int(input())
INF = int(1e9)

results = []

for _ in range(TC):
    n, m, w = map(int, input().split())
    edges = []

    # 도로: 양방향
    for _ in range(m):
        a, b, t = map(int, input().split())
        edges.append((a, b, t))
        edges.append((b, a, t))

    # 웜홀: 단방향, 음수 가중치
    for _ in range(w):
        a, b, t = map(int, input().split())
        edges.append((a, b, -t))

    # 모든 정점이 출발점이 될 수 있으므로 전부 0으로 초기화
    dist = [0] * (n + 1)
    has_negative_cycle = False

    # Bellman-Ford: n번 반복
    for i in range(n):
        updated = False
        for u, v, time in edges:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                updated = True
                # n번째 반복(i == n-1)에 갱신 발생 → 음수 사이클
                if i == n - 1:
                    has_negative_cycle = True
                    break
        # 더 이상 갱신이 없으면 조기 종료
        if not updated:
            break

    results.append("YES" if has_negative_cycle else "NO")

# 최종 출력
print("\n".join(results))
