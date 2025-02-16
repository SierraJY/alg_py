import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

# 1 : 상, 2: 하, 3: 좌, 4 : 우
def is_possible_link(now_pos, d, now_matrix):
    """
    연결 가능성 평가 함수
    :param now_pos: 현재 코어 위치
    :param d: 연결 방향
    :param now_matrix:
    :return:
    """
    if d == 1 :
        for r in range(now_pos[0]-1, -1,-1):
            if now_matrix[r][now_pos[1]] != 0 :
                return False

    elif d == 2 :
        for r in range(now_pos[0]+1, N):
            if now_matrix[r][now_pos[1]] != 0 :
                return False

    elif d == 3:
        for c in range(now_pos[1]-1, -1, -1):
            if now_matrix[now_pos[0]][c] != 0 :
                return False
    elif d == 4:
        for c in range(now_pos[1]+1, N):
            if now_matrix[now_pos[0]][c] != 0:
                return False

    return True

def link_wire(now_pos, d, now_matrix):
    """
    실제 연결을 담당하는 함수
    :param now_pos: 현재 코어 위치
    :param d: 연결할 방향
    :param now_matrix:
    :return:
    """
    linked_len = 0

    if d == 1:
        for r in range(now_pos[0] - 1, -1, -1):
            now_matrix[r][now_pos[1]] = 2
            linked_len += 1

    elif d == 2:
        for r in range(now_pos[0] + 1, N):
            now_matrix[r][now_pos[1]] = 2
            linked_len += 1

    elif d == 3:
        for c in range(now_pos[1] - 1, -1, -1):
            now_matrix[now_pos[0]][c] = 2
            linked_len += 1

    elif d == 4:
        for c in range(now_pos[1] + 1, N):
            now_matrix[now_pos[0]][c] = 2
            linked_len += 1

    return linked_len

def dfs(now_core_i, now_core_cnt, now_wire_len, now_matrix):
    global max_core_cnt, max_core_min_wire_len

    if now_core_i == core_cnt:
        if now_core_cnt > max_core_cnt:
            max_core_cnt = now_core_cnt
            max_core_min_wire_len = now_wire_len
        elif now_core_cnt == max_core_cnt:
            max_core_min_wire_len = min(max_core_min_wire_len, now_wire_len)
        return

    if (core_cnt - now_core_i) + now_core_cnt < max_core_cnt :
        return

    for i in range(now_core_i+1, core_cnt + 1):
        now_r = core_pos_list[now_core_i][0]
        now_c = core_pos_list[now_core_i][1]
        for d in range(5):
            copy_matrix = [r[:] for r in now_matrix]
            if d == 0: # 현재 코어를 연결하지 않는 경우
                dfs(i, now_core_cnt, now_wire_len, copy_matrix)
            elif is_possible_link((now_r, now_c), d, copy_matrix):
                new_linked_len = link_wire((now_r,now_c), d, copy_matrix)
                dfs(i, now_core_cnt + 1, now_wire_len + new_linked_len, copy_matrix)

for t in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    core_pos_list = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                if not (r == 0 or r == N - 1 or c == 0 or c == N - 1):
                    core_pos_list.append((r, c))

    core_cnt = len(core_pos_list)

    max_core_cnt = -1
    max_core_min_wire_len = 0

    dfs(0, 0, 0, matrix)
    print(f"#{t+1} {max_core_min_wire_len}")


# 문제 & 알고리즘
# <다른 코어를 연결하는 전선이 현재 코어를 끊어 먹을지 and 지금 연결 전선이 최대 전선합이 될지 어떻게 암?>
# 수학적인 방식으로 불가
# 완전 탐색 DFS(재귀) & 백트래킹(copy)

# <재귀 어떻게 시작할 것인가?>
# 미리 코어 리스트를 만들어둠
# !!! 가장자리 코어는 최대 전선 길이합에 영향X이므로, 그냥 장애물 취급 !!!

# <현재 코어 연결 가능성과 필요 전선 길이 계산>
# 조건문 & 반복문