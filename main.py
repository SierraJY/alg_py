# 픽셀 수 구하기

# 5 * 5 이차원 배열에 모니터 화면을 표현합니다 모니터의 화변은 최초 검정색과 흰색으로만 표현되어 있습니다
# 검정색은 1, 흰색은 0으로 표현됩니다
# 상하좌우로 1(검정색)이 연결되어 있으면 한 영역으로 간주합니다
# 매개변수 board에 모니터 화면의 격자정보가 주어지면 검정색으로 칠해진 각 영역의 픽셀수를
# 순서대로 배열에 담아 반환하세요 영역의 순서는 각 영역의 행번호 열번호가 가장 작은 픽셀을
# 기준으로 행번호가 작은 것부터이며 행번호가 같을 경우 열 번호가 작은 영역 순으로 배열에 담습니다

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def solution(board):

    pixel_cnts = []
    def dfs(coord): # 명확한 실행 조건이 있는 재귀함수이기 떄문에, 종료조건 필요없음

        cnt = 1 # 한 번이라도 호출되면 해당 영역 픽셀 개수 1개 보장 / 주변에 검정색이 없으면 1만 반환하게됨

        for d in range(4):
            nr = coord[0] + dr[d]
            nc = coord[1] + dc[d]

            if (nr >= 0 and nc >= 0) and (nr < len(board) and nc < len(board)) and board[nr][nc] == 1:
                board[nr][nc] = 'c'
                cnt += dfs((nr,nc))

        return cnt

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1 :
                board[r][c] = 'c'
                pixel_cnts.append(dfs((r,c)))

    return pixel_cnts

print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

# how
# 재귀함수 사용
# 검정색인 픽셀에 대하여 네 방향의 픽셀을 확인하는 함수를 재귀적으로 실행시킨다
