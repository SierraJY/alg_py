import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []

doyeon = None

for r in range(N):
    row = input().strip()
    for c in range(M):
        if row[c] == 'I':
            doyeon = (r, c)

    matrix.append(row)

can_meet = 0
queue = deque()
queue.append(doyeon)
visited = [[False for _ in range(M)]for _ in range(N)]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
while queue:
    now_queue_level = len(queue)
    for _ in range(now_queue_level):
        popped = queue.popleft()

        if matrix[popped[0]][popped[1]] == 'P':
            can_meet += 1

        for d in range(4):
            nr = popped[0] + dr[d]
            nc = popped[1] + dc[d]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False and matrix[nr][nc] != 'X':
                queue.append((nr,nc))
                visited[nr][nc] = True

if can_meet:
    print(can_meet)
else:
    print('TT')






# 도연이 위치 시작점으로 BFS