from collections import deque

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def bfs(coord, board):
    queue = deque()
    queue.append(coord)

    level = 0 # 현재 문제에서 필요없는 변수

    while queue:
        now_level_cnt = len(queue)
        for _ in range(now_level_cnt):
            v = queue.popleft()
            for d in range(4):
                nr = v[0] + dr[d]
                nc = v[1] + dc[d]
                if 0 <= nr < len(board) and 0 <= nc < len(board) and board[nr][nc] == 1:
                    board[nr][nc] = 'c'
                    queue.append((nr,nc))

        level += 1

def solution(board):

    cnt = 0

    for r in range(len(board)):
        for c in range(len(board)) :
            if board[r][c] == 1:
                board[r][c] = 'c'
                cnt += 1
                bfs((r,c), board)

    return cnt


print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

# how
# 우선 검정색 영역의 기준점 찾음(맨 오른쪽 위인 칸이 될 것)
# 그 영역으로부터 1거리 떨어진 영역에서 부터, 검정인지 확인 후 Queue에 넣음
# Queue가 비워질 때 까지 반복

# 알게된 것
# 같은 문제의 dfs or stack 방식과는 영역을 확인해나가는 방향(?)이 다름