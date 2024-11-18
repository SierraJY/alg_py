from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for (v1, v2) in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0 for _ in range(n + 1)]
    queue = deque()
    queue.append(1)
    now_level = 0
    visited[1] = 1 # 시작점 방문 표시

    while queue:
        now_level += 1
        now_level_cnt = len(queue)

        for _ in range(now_level_cnt):
            popped = queue.popleft()
            for v in graph[popped]:
                if visited[v] == 0:
                    queue.append(v)
                    visited[v] = now_level

    return visited.count(max(visited))

# what
# 1번 노드에서 가장 멀리 떨어진 노드가 몇 개인지를 return

# how
# 최단 경로 개념 필요 : BFS
# visited에 1표시 말고 1번 노드에 떨어진 정도인 now_level을 넣음
