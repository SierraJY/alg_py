import sys

sys.stdin = open('input.txt', 'r')
n, m = map(int, sys.stdin.readline().split())

INF = int(1e9)
graph = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n) : graph[i][i] = 0

first_visit = [['-' for _ in range(n)] for _ in range(n)]

for _ in range(m):
    v1, v2, w = map(int, sys.stdin.readline().split())
    graph[v1 - 1][v2 - 1] = w
    graph[v2 - 1][v1 - 1] = w
    first_visit[v1 - 1][v2 - 1] = str(v2)
    first_visit[v2 - 1][v1 - 1] = str(v1)

for mid in range(n):
    for v1 in range(n):
        for v2 in range(n):
            if graph[v1][mid] + graph[mid][v2] < graph[v1][v2]:
                graph[v1][v2] = graph[v1][mid] + graph[mid][v2]
                first_visit[v1][v2] = first_visit[v1][mid]

for row in first_visit:
    print(" ".join(row))

# what
# 한 집하장에서 다른 집하장으로 최단경로로
# 화물을 이동시키키 위해 가장 먼저 거쳐야 하는 집하장 표 작성

# how
# 플로이드 와샬

# 주의할 것
# 플로이드 와샬에서는 인접행렬로 그래프를 표현하는 것이 좋음