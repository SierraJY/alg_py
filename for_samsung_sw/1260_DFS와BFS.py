# note : BFS에서 now_level_cnt는 반드시 만들지 않아도 된다
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False for _ in range(N+1)]
def dfs(node_a):
    print(node_a, end=" ")
    visited[node_a] = True
    for node_b in graph[node_a]:
        if not visited[node_b]:
            dfs(node_b)

dfs(V)
print()

from collections import deque

visited = [False for _ in range(N+1)]

def bfs(node_a):
    queue = deque()
    queue.append(node_a)
    visited[node_a] = True
    while queue:
        popped = queue.popleft()
        print(popped, end=" ")
        for node_b in graph[popped]:
            if not visited[node_b]:
                queue.append(node_b)
                visited[node_b] = True

bfs(V)