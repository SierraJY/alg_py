import sys
import heapq

sys.stdin = open('input.txt', 'r')

N, M, K, X = map(int, sys.stdin.readline().split())

INF = int(1e9)
graph = [[]for _ in range(N)]
distance = [INF for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1-1].append(v2-1)

X -= 1
distance[X] = 0
heap = [(0, X)]

while heap:
    d, v1 = heapq.heappop(heap)

    if d < distance[v1] :
        distance[v1] = d

    for v2 in graph[v1]:
        if 1 + d < distance[v2]:
            heapq.heappush(heap, (1 + d, v2 ))

if K not in distance : print(-1)
else:
    for i in range(N):
        if distance[i] == K : print(i+1)



# what
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 노드 중에서,
# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.

# how
# 다익스트라 알고리즘

# 주의할 것
# 모든 도로의 거리는 1