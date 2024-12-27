import sys
import heapq

sys.stdin = open('input.txt', 'r')

# 땅 후보의 개수
N = int(sys.stdin.readline())
# 친구들 위치, 친구들은 N개의 땅 중 하나에 사는 것이 보장된다. (같은 위치에서 살 수 있다)
A, B, C = map(int, sys.stdin.readline().split())
# 땅과 땅을 잇는 도로의 개수
M = int(sys.stdin.readline())

# 1부터 시작하는 그래프
graph = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2, w = map(int, sys.stdin.readline().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

INF = 1e9
def dijkstra(f_home):
    distance = [INF for _ in range(N+1)]
    distance[f_home] = 0
    q = [(0, f_home)]
    while q:
        d, v1 = heapq.heappop(q)

        if d > distance[v1] : continue

        for (v2, w) in graph[v1]:
            if d + w < distance[v2] :
                distance[v2] = d + w
                heapq.heappush(q, (d + w, v2))

    return distance

A_distance = dijkstra(A)
B_distance = dijkstra(B)
C_distance = dijkstra(C)

max_d_c = 0 # 최대 거리 후보
max_d = 0 # 최대 거리 후보의 거리

for c in range(1, N+1):
    if c in [A, B, C] : continue
    c_min_d = min([A_distance[c], B_distance[c], C_distance[c]])
    if c_min_d > max_d:
        max_d = c_min_d
        max_d_c = c

print(max_d_c)

# what
# 친구들 A, B, C와 가장 먼 곳에 떨어진 집 구하기 (여러곳이라면 땅 번호가 가장 작은 곳)
# 가장 먼 곳은 가장 가까운 친구의 집까지의 거리를 기준으로 정함
# 예를 들어, X 위치에 있는 집에서 친구들의 집까지의 거리가 각각 3, 5, 4이라 가정하고
# Y 위치에 있는 집에서 친구들의 집까지의 거리가 각각 5, 7, 2라고 하자.
# 이때, 친구들의 집으로부터 땅 X와 땅 Y 중 더 먼 곳은 땅은 X이다.
# 왜냐하면 X에서 가장 가까운 친구의 집까지의 거리는 3이고, Y에서는 2이기 때문이다.

# how
# 그래프
# A, B, C에서 시작하여 다른 모든 노드까지 최단 거리를 구함
# 그 결과를 바탕으로 가장 멀리 떨어진 곳을 찾는다

# 주의할 것
# 생각해보면
# 모든 노드에서 다익스트라를 사용 하기보다
# A, B, C에서 세 번 다익스트라를 사용하는 것이 더 효율적