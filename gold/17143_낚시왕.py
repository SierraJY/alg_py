import sys
from collections import defaultdict, deque

sys.stdin = open(0, 'r')
input = sys.stdin.readline

def get_next_pos_dir(pos, dir, move_cnt, max_pos):

    # 원상태로 돌아오기 위한 칸 수로 나누어서 직접 움직일 칸 수만 남김
    move_rest = move_cnt % (2 * max_pos - 2)

    if dir in [1, 4]:
        mode = -1
    elif dir in [2, 3]:
        mode = 1

    for _ in range(move_rest):
        if pos + mode < 0 or pos + mode == max_pos:
            mode *= -1

        pos += mode

    # mode 기준으로 최종 방향만 재매핑 (원래 dir 안 봄)
    if dir in [1, 2]:  # 상하 이동
        return pos, 2 if mode == 1 else 1
    else:  # 좌우 이동
        return pos, 3 if mode == 1 else 4


matrix = defaultdict(deque)

R, C, M = map(int, input().split())

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    matrix[(r-1, c-1)].append((s, d, z))  # 0-indexed 저장

catch = 0

for king in range(C):  # 열 단위로 낚시왕 이동
    keys = list(matrix.keys())
    min_r = R

    # 해당 열에서 가장 위에 있는 상어 찾기
    for r, c in keys:
        if c == king:
            min_r = min(min_r, r)

    # 상어 잡기
    if min_r != R:
        catch += matrix[(min_r, king)][0][2]
        del matrix[(min_r, king)]

    # 상어 이동 처리
    new_matrix = defaultdict(deque)
    for k in keys:
        if not matrix[k]:
            continue

        s, d, z = matrix[k].popleft()

        if d in [1, 2]:  # 세로 방향
            new_r, new_d = get_next_pos_dir(k[0], d, s, R)
            new_c = k[1]
        else:  # 가로 방향
            new_c, new_d = get_next_pos_dir(k[1], d, s, C)
            new_r = k[0]

        new_matrix[(new_r, new_c)].append((s, new_d, z))

    # 겹치는 상어 처리 (가장 큰 상어만 남김)
    for k in new_matrix:
        if len(new_matrix[k]) > 1:
            max_shark = max(new_matrix[k], key=lambda x: x[2])
            new_matrix[k].clear()
            new_matrix[k].append(max_shark)

    matrix = new_matrix  # 이동 후 상태 갱신

print(catch)

# 아이디어 & 알고리즘
# 상어 위치 관리?
# => 딕셔너리

# 상어 회전 처리?
# => 수학적으로 일부 처리 -> 남은 건 직접 움직이기