# note : DFS의 visited check 타이밍은 직접 방문 후에 해도 가능
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
E = int(input())

graph = [[]for _ in range(N+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]

def dfs(node_a):
    visited[node_a] = True
    for node_b in graph[node_a]:
        if not visited[node_b]:
            dfs(node_b)

dfs(1)
print(sum(visited)-1)