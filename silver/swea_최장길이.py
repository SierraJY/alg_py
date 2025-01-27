import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

def dfs(graph, visited, p_node, p_cnt):
    max_cnt = p_cnt
    visited[p_node] = 1

    for v2 in graph[p_node]:
        if visited[v2] == 0:
            max_cnt = max(max_cnt, dfs(graph, visited, v2, p_cnt+1))

    visited[p_node] = 0
    return  max_cnt

for t in range(T):
    N, M = map(int,input().split())
    # 그래프 1부터 사용
    visited = [0 for _ in range(N + 1)]
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    max_cnt = 0
    for v in range(1,N+1):
        max_cnt = max(max_cnt, dfs(graph, visited, v, 1))

    print(f"#{t+1} {max_cnt}")


# what
# 노드가 가장 많은 개수의 경로의 노드 개수
# 무방향 그래프

# how
# 재귀 + 백트래킹
# 스택보다 재귀인 이유
# 한 경로로 갔다가 분기로 다시 되돌아 올 경우, 방문 표시를 끄면서 돌아와야함

# 주의할 것
# visited 끄는 것을 어디서 할 것인지 (백트래킹 처리를 어디서?)