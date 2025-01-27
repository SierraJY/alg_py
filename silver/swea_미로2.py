import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def bfs(matrix):
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)
    visited = [[0 for _ in range(100)] for _ in range(100)]
    q = deque()
    q.append((1,1))

    while q:
        now_q_cnt  = len(q)
        for _ in range(now_q_cnt):
            popped = q.popleft()
            for i in range(4):
                nr = popped[0] + dr[i]
                nc = popped[1] + dc[i]
                # 범위 내이고, 방문하지 않았고, 벽도 아닌 곳만
                if (0 <= nr <= 99) and (0 <= nc <= 99) and visited[nr][nc] == 0 and matrix[nr][nc] != '1':
                    q.append((nr,nc))
                    visited[nr][nc] = 1
                    if matrix[nr][nc] == '3' : return 1
    return 0

for t in range(10):
    input()
    matrix = [input() for _ in range(100)]
    print(f"#{t+1} {bfs(matrix)}")

# 알게된 것
# swea 문제를 어떻게든 조금 더 빨리 풀 수 있는 방법 : intput = sys.stdin.readline()
# matrix의 행을 문자열 공백 없이 줘버리는 swea 문제의 더러움을 느낄 수 있었음