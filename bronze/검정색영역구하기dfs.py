def solution(board):

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    cnt = 0 # 영역개수
    stack = []

    def check_around(coordinate): # 네 방향의 칸 확인 후, 1이면 'c'로 바꾼 후 해당 좌표 스택에 append
        for d in range(4):
            nr = coordinate[0] + dr[d]
            nc = coordinate[1] + dc[d]
            if (0 <= nr and 0 <= nc) and (len(board) > nr and len(board) > nc) and board[nr][nc] == 1:
                board[nr][nc] = 'c'
                stack.append((nr, nc))

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1 :
                board[r][c] = 'c'
                cnt += 1
                stack.append((r,c))

            while stack:
                check_around(stack.pop())

    return cnt


print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

# how
# 일단 해당 칸이 검정색인지 확인 후 'c'로 변환 그리고 영역 개수 + 1
# 해당 칸의 상하좌우 칸들이 1이면 'c'로 변환 후 스택에 append
# 스택 비워질 때 까지 꺼내서 바로 위의 과정 반복

# 다른 방식
# 재귀로 풀면?
# 일단 해당 칸이 검정색인지 확인 후 'c'로 변환 그리고 영역 개수 + 1
# 해당 칸이 0이면 종료, 아니면 네 방향 칸에 대해 다시 체크하는 함수 재귀 실행

