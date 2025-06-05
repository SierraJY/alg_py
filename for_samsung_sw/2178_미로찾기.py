# note : now_level_cnt가 필요한 경우와 visited check 타이밍

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [input().strip() for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

from collections import deque

dr = (-1, 0 , 1, 0)
dc = (0, 1, 0, -1)

def bfs(start):
    queue = deque()
    queue.append(start)
    level = 1
    visited[0][0] = True

    while queue:

        now_level_cnt = len(queue)
        level += 1

        for _ in range(now_level_cnt):
            popped = queue.popleft()

            for d in range(4):
                nr = popped[0] + dr[d]
                nc = popped[1] + dc[d]

                if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == '1' and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    if nr == N - 1 and nc == M - 1:
                        print(level)
                        return
                    queue.append((nr,nc))

bfs((0,0))



