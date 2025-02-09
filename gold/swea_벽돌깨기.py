import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

def down_tiles(matrix):
    """
    폭발이 발생한 후, 벽돌을 내리는 함수
    :param matrix: 맵
    :return: 없음
    """
    for c in range(0, C):
        zero_cnt = 0 # 현재 r까지 올라오면서 있었던 0의 개수
        for r in range(R-1, -1, -1):
            if matrix[r][c] == 0 :
                zero_cnt += 1
            else:
                if zero_cnt == 0 : # 연이어 0이 아닌 경우
                    continue
                else: # 0이 있다가 0이 아닌 수가 나온 경우
                    matrix[r+zero_cnt][c] = matrix[r][c]
                    matrix[r][c] = 0

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
def boom_dfs(boom_r, boom_c, matrix):
    """
    폭발이 전이(dfs(재귀 방식))되도록하고, 터진 벽돌 개수를 반환하는 함수
    :param boom_r: 폭발 좌표 r
    :param boom_c:  폭발 좌표 c
    :param matrix: 맵
    :return: 깨진 벽돌의 개수
    """
    power = matrix[boom_r][boom_c] # 터지는 세기
    matrix[boom_r][boom_c] = 0

    if power == 1 :
        return 1

    elif power > 1:
        cnt = 1
        for p in range(1, power):
            for i in range(4):
                nr = boom_r + dr[i] * p
                nc = boom_c+ dc[i] * p
                if 0<= nr < R and 0 <= nc < C and matrix[nr][nc] != 0:
                    cnt += boom_dfs(nr, nc, matrix)
        return cnt

def throwing(throw_cnt, now_boom_cnt, now_matrix):
    """
    구슬을 던지는 함수, dfs(재귀 방식)+백트래킹(맵을 복사해서 넘기는 방식)으로 구현
    :param throw_cnt: 던진 횟수
    :param now_boom_cnt: 현재 까지 깨진 벽돌 수
    :param now_matrix: 현재 맵 상태
    :return: 없음, 조건 만족하면 깨진 최대 벽돌 개수만 갱신
    """
    global max_boomed

    if throw_cnt == N:
        if now_boom_cnt > max_boomed :
            max_boomed = now_boom_cnt
        return

    if any([any(r) for r in now_matrix]) == False :
        if now_boom_cnt > max_boomed :
            max_boomed = now_boom_cnt
        return

    for next_c in range(C):
        for next_r in range(R):
            copy_matrix = [r[:] for r in now_matrix]
            if copy_matrix[next_r][next_c] != 0:
                boom_cnt = boom_dfs(next_r, next_c, copy_matrix)
                down_tiles(copy_matrix)
                throwing(throw_cnt+1, now_boom_cnt + boom_cnt, copy_matrix)
                break

for t in range(T):
    N, C, R = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(R)]

    max_boomed = 0 #최대로 부셨을 때 개수

    initial_state = 0 #초기 원래 벽돌 개수
    for r in range(R):
        for c in range(C):
            if matrix[r][c] != 0 : initial_state += 1

    throwing(0, 0, matrix)

    print(f"#{t+1} {initial_state - max_boomed}")

# IDEA
# <어디로 어떤 순서로 발사해야 가장 많이 없앨 수 있나?>
# 수학적 방식으로 미리 얼마나 깰 수 있는지 알 수 없음므로, 완전탐색 필요
# => 완전탐색DFS & 백트래킹
# 발사 위치는 반복문으로
# <폭발 후, 백트래킹을 위해 matrix 상태 변경과 다시 되돌리기는?>
# => matrix copy
# <폭발을 전이 시키는 방법은?>
# => dfs(재귀)
# <폭발 후, 떨어지는 벽돌들은?>
# => 반복문

# 주의할 것
# 관성적으로 풀려하지말것, dfs에 반드시 좌표를 넘겨야한다는 고정관념 X

# 알게된 것
# 매 단계마다 현재 상태의 맵을 복사하여 분기별로 독립된 상태를 유지하는 것
# Python 2차원 배열 빠르게 깊은 복사하는 법(deepcopy 함수보다 빠름)