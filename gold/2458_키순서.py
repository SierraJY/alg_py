import sys

sys.stdin = open('input.txt', 'r')
V_N , E_N = map(int, sys.stdin.readline().split())

INF = int(1e9)
# 0부터 사용 X
graph = [[INF for _ in range(V_N)] for _ in range(V_N)]
for i in range(V_N) : graph[i][i] = 0

for _ in range(E_N):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1-1][v2-1] = -1 #v1이 v2보다 키가 작음
    graph[v2-1][v1-1] = 1 #v2가 v1보다 키가 큼

for mid in range(0, V_N):
    for v1 in range(0, V_N):
        for v2 in range(0, V_N):
            if graph[v1][v2] == INF:
                if graph[v1][mid] == -1 and graph[mid][v2] == -1:
                    graph[v1][v2] = -1
                    graph[v2][v1] = 1
                elif graph[v1][mid] == 1 and graph[mid][v2] == 1:
                    graph[v1][v2] = 1
                    graph[v2][v1] = -1

dont_know_cnt = 0
for row in graph:
    if INF in row : dont_know_cnt += 1

print(V_N - dont_know_cnt)

