# 텀 프로젝트
import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(i):
    global team_members

    visited[i] = True
    cycle.append(i)
    select = selected[i]

    if visited[select]:
        if select in cycle:
            team_members += cycle[cycle.index(select):]
        return
    else:
        dfs(select)

t = int(input())

for _ in range(t):
    n = int(input())
    selected = [0] + list(map(int, input().split()))

    visited = [True] + [False] * n
    team_members = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(team_members))