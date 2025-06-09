# note : 반복이 많아지면 재귀방식 DFS가 훨씬 느리다
# note : recursion error -> sys.setrecursionlimit로 해제 or BFS
# note2 : "아무 지역도 물에 잠기지 않을 수도 있다"

import sys

sys.setrecursionlimit(100*100)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
matrix = []
heights = set()
heights.add(0)

for _ in range(N):
    row = list(map(int, input().split()))
    heights.update(row)
    matrix.append(row)


dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def dfs(node_a, flag):
    visited[node_a[0]][node_a[1]] = True

    for d in range(4):
        nr = node_a[0] + dr[d]
        nc = node_a[1] + dc[d]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False and matrix[nr][nc] > flag:
            dfs((nr,nc), flag)

    return

max_cnt = 0

for flag in heights:
    now_cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if matrix[r][c] > flag and visited[r][c] == False:
                now_cnt += 1
                dfs((r,c), flag)

    # print(flag, '-----------')
    # for v in visited:
    #     print(v)
    # print('-----------')
    max_cnt = max(max_cnt, now_cnt)

print(max_cnt)
