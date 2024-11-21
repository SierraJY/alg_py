import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt', 'r')
V_N , E_N = map(int, sys.stdin.readline().split())

start_v = int(sys.stdin.readline())

graph = [[]for _ in range(V_N+1)]
for _ in range(E_N):
    v1, v2, weight = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, weight))

INF = int(1e9)
d = [INF for _ in range(V_N+1)]
d[start_v] = 0
pq = [(0, start_v)]

while pq:
    distance, a = heappop(pq)

    if d[a] < distance : continue

    for (b,w) in graph[a]:
        if distance + w < d[b]:
            d[b] = distance + w
            heappush(pq, (distance + w, b))

for i in range(1, len(d)):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])
