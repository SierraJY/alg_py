# note : BFS에서 탐색을 종료하고 Now_level을 반환해야하는 타이밍

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
p1, p2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

visited = [False for _ in range(N+1)]
c = 0
queue = deque()
queue.append(p1)
now_level = 1
visited[p1] = True

while queue:
    now_level_cnt = len(queue)

    for _ in range(now_level_cnt):
        popped = queue.popleft()

        for child in graph[popped]:
            if not visited[child]:
                if child == p2:
                    c = now_level
                    break
                queue.append(child)
                visited[child] = True

        if c:
            break

    if c:
        break

    now_level += 1

if c:
    print(c)
else:
    print(-1)
