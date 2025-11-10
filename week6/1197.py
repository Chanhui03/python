# 최소 스패닝 트리

import sys
input = sys.stdin.readline

# 런타임 에러 방지용 재귀 한도 설정
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    # 크루스칼 알고리즘이라서 간선은 한번만 저장
    edges.append((c, a, b))

# 간선을 비용 기준으로 오름차순 정렬
edges.sort()

# 부모 테이블 초기화 (0 ~ v) 0번 노드는 편의상 저장
parent = [i for i in range(v + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

result = 0

# 사이클이 생기면 안되므로 모든 간선을 확인해도 됨
for edge in edges:
    weight, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += weight

print(result)
