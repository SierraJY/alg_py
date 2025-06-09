# note : 같은 레벨에 대해서 녹은 빙산은 동시에 처리, 숨바꼭질2 같은 느낌
# note : 빙산이 녹은 경우가 있을 때만 연결성 확인
# note : sys가 불가능한 환경에서 Stack을 통한 DFS 구현

import sys
from inspect import stack

sys.stdin = open('input.txt', 'r')
# sys.setrecursionlimit(300*300)
input = sys.stdin.readline

N, M = map(int, input().split())

from collections import deque

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
matrix = []
queue = deque()
now_level = 1
find = False

for r in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    for c in range(M):
        if row[c] != 0 :
            queue.append((r,c))

def dfs(node_a):
    stack = [node_a]
    visited[node_a[0]][node_a[1]] = True

    while stack:
        r, c = stack.pop()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and matrix[nr][nc] != 0:
                visited[nr][nc] = True
                stack.append((nr, nc))

# def dfs(node_a):
#     visited[node_a[0]][node_a[1]] = True
#
#     for d in range(4):
#         nr = node_a[0] + dr[d]
#         nc = node_a[1] + dc[d]
#
#         if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False and matrix[nr][nc] != 0:
#             dfs((nr,nc))

while queue:
    now_level_cnt = len(queue)
    tmp_zeros = []
    ice_cnt = 0

    for _ in range(now_level_cnt):
        popped = queue.popleft()

        for d in range(4):
            nr = popped[0] + dr[d]
            nc = popped[1] + dc[d]

            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 0:
                matrix[popped[0]][popped[1]] -= 1
                if matrix[popped[0]][popped[1]] == 0:
                    matrix[popped[0]][popped[1]] = -1
                    tmp_zeros.append(popped)
                    break

        if matrix[popped[0]][popped[1]] != -1:
            queue.append(popped)

    if tmp_zeros:

        for z_r, z_c in tmp_zeros:
            matrix[z_r][z_c] = 0

        visited = [[False for _ in range(M)] for _ in range(N)]

        for ice in queue:
            if not visited[ice[0]][ice[1]]:
                dfs(ice)
                ice_cnt += 1
                if ice_cnt >= 2:
                    find = True
                    break



    # print(now_level, ice_cnt, "-----------------------")
    # for v in matrix:
    #     print(v)
    # print("-----------------------")

    if ice_cnt >= 2:
        break

    now_level += 1

if find:
    print(now_level)
else:
    print(0)