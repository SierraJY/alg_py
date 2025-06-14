# note : BFS 최단 경로 정보를 반환해야하는 경우, visited에 이전 지점 저장해두기
# note : 대각선 지점도 고려하는 경우, dr/dc 구성 및 모듈로 연산

# 반례 : 메두사가 전사에게 도달한 것은 공격 횟수로 안침
# 반례 : 전사가 움직일 수 없는 경우, 새로운 전사 상황 매트릭스에 반영해야함

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int,input().split())
sr, sc, er, ec = map(int,input().split())
warriors = list(map(int,input().split()))
warrior_matrix = [[0 for _ in range(N)] for _ in range(N)]
for i in range(0, 2*M, 2):
    warrior_matrix[warriors[i]][warriors[i+1]] += 1
matrix = [list(map(int,input().split())) for _ in range(N)]

# [구현 1] 메두사 이동
# 메두사는  도로()만 따라 최단 경로로 공원까지 이동
# 최단경로 여러가지라면 상->하->좌->우
# 도달이 불가능할 수도 있음
# 메두사가 이동한 칸에 전사가 있을 경우 전사는 사라짐
def find_m_route(start_pos, end_pos):
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    queue = deque()
    queue.append(start_pos)
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[start_pos[0]][start_pos[1]] = start_pos

    while queue:
        popped = queue.popleft()

        if popped[0] == end_pos[0] and popped[1] == end_pos[1]:
            route = []
            prev = visited[popped[0]][popped[1]]

            while prev[0] != start_pos[0] or prev[1] != start_pos[1]:
                route.append(prev)
                prev = visited[prev[0]][prev[1]]

            return route[::-1]

        for d in range(4):
            nr = popped[0] + dr[d]
            nc = popped[1] + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and matrix[nr][nc] == 0:
                visited[nr][nc] = popped
                queue.append((nr,nc))

    return -1

# [구현 2] 메두사 시선
# 메두사는 상, 하, 좌, 우 하나의 방향을 선택해 바라봄(전사를 가장 많이 볼 수 있는 방향으로)
# 시야각의 90도, 시야각에 있더라도 다른 전사에게 가려진 전사는 보이지 않음
# 가려지는 범위는 가리는 전사와 상대적인 위치에 의해 결정
# 상,하,좌,우,대각선 8방향으로 나누엇을 때, 메두사로 부터 8방향 중 한 방향에 전사가 위치해 있다면
# 그 전사가 동일한 방향을 바라본 범위에 포함된 칸은 메두사에게 보이지 않음
# 메두사가 본 전사(들)은 돌로 변해 현재 턴에 움직일 수 없음
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

def check_safe(w_pos, viewed, d, diag):
    vr = w_pos[0] + dr[d]
    vc = w_pos[1] + dc[d]

    while 0 <= vr < N and 0 <= vc < N and viewed[vr][vc] == False:
        viewed[vr][vc] = 3
        vr += dr[d]
        vc += dc[d]

    if diag != -1:
        diagr = w_pos[0] + dr[diag]
        diagc = w_pos[1] + dc[diag]

        while 0 <= diagr < N and 0 <= diagc < N and viewed[diagr][diagc] == False:
            viewed[diagr][diagc] = 3

            vr = diagr + dr[d]
            vc = diagc + dc[d]

            while 0 <= vr < N and 0 <= vc < N and viewed[vr][vc] == False:
                viewed[vr][vc] = 3
                vr += dr[d]
                vc += dc[d]

            diagr += dr[diag]
            diagc += dc[diag]

def check_straight(v_pos, viewed, d, diag):
    cnt = 0

    if warrior_matrix[v_pos[0]][v_pos[1]] > 0 and viewed[v_pos[0]][v_pos[1]] == 0:
        # print(v_pos)
        cnt += warrior_matrix[v_pos[0]][v_pos[1]]
        viewed[v_pos[0]][v_pos[1]] = 2
        check_safe(v_pos, viewed, d, diag)
        return cnt
    else:
        viewed[v_pos[0]][v_pos[1]] = 1

    vr = v_pos[0] + dr[d]
    vc = v_pos[1] + dc[d]

    while 0 <= vr < N and 0 <= vc < N and viewed[vr][vc] == False:
        if warrior_matrix[vr][vc]:
            # print(vr,vc)
            cnt += warrior_matrix[vr][vc]
            viewed[vr][vc] = 2
            check_safe((vr,vc), viewed, d, diag)
            break
        else:
            viewed[vr][vc] = 1

        vr += dr[d]
        vc += dc[d]

    return cnt

def medusa_see(m_pos):
    # 0 : 아직 보지 않거나 시야각 제외
    # 1 : 시야각 포함
    # 2 : 돌이된 위치
    # 3 : 안전한 위치
    max_cnt = -1
    max_cnt_viewed = None

    for d in (0, 4, 6, 2):
        viewed = [[False for _ in range(N)] for _ in range(N)]
        # print(d, "----------------")
        d_cnt = 0
        # [1] d 방향으로 체크
        vr = m_pos[0] + dr[d]
        vc = m_pos[1] + dc[d]
        if 0 <= vr < N and 0 <= vc < N:
            d_cnt += check_straight((vr,vc), viewed, d, -1)

        # [2] diag 방향으로 체크
        for diag in ((d-1)%8, (d+1)%8):
            diagr = m_pos[0] + dr[diag]
            diagc = m_pos[1] + dc[diag]

            while 0 <= diagr < N and 0 <= diagc < N and viewed[diagr][diagc] == False:
                d_cnt += check_straight((diagr, diagc), viewed, d, diag)
                diagr += dr[diag]
                diagc += dc[diag]

        # print(d_cnt)
        # print("-----------")
        # for r in viewed:
        #     print(r)

        if d_cnt > max_cnt:
            max_cnt = d_cnt
            max_cnt_viewed = viewed[:]

    return max_cnt, max_cnt_viewed

# # medusa_see((1,2))
# for r in warrior_matrix:
#     print(r)
# print(medusa_see((1,2)))

# [구현 3] 전사들의 이동
# 용사들은 도로/비도로 구분X
# 돌로 변하지 않은 전사들은 메두사를 향해 최대 두 칸 이동
# 메두사와 거리를 줄일 수 있는 방향으로 이동
# 방향이 두 개 이상일 경우 상하좌우 우선순위
# 격자의 바깥 및 메두사의 시야 위치 불가
def warrior_move(move_i, w_pos, m_pos, viewed, new_warrior_matrix):
    move_cnt = 0
    moved = False  # 이동 여부 추적
    directions = None
    if move_i == 0:
        directions = (0, 4, 6, 2)  # 상하좌우
    elif move_i == 1:
        directions = (6, 2, 0, 4)  # 좌우상하

    for d in directions:
        nr = w_pos[0] + dr[d]
        nc = w_pos[1] + dc[d]

        if 0 <= nr < N and 0 <= nc < N and (viewed[nr][nc] == 0 or viewed[nr][nc] == 3):
            org_distance = abs(w_pos[0] - m_pos[0]) + abs(w_pos[1] - m_pos[1])
            next_distance = abs(nr - m_pos[0]) + abs(nc - m_pos[1])
            if next_distance < org_distance:
                # print(org_distance, next_distance, d)
                move_cnt += warrior_matrix[w_pos[0]][w_pos[1]]
                new_warrior_matrix[nr][nc] += warrior_matrix[w_pos[0]][w_pos[1]]
                moved = True  # 이동 완료
                break

    # 이동하지 못한 경우 원래 위치에 유지
    if not moved:
        new_warrior_matrix[w_pos[0]][w_pos[1]] += warrior_matrix[w_pos[0]][w_pos[1]]

    return move_cnt

# max_cnt, max_cnt_viewed = medusa_see((1,2))
# move_cnt = 0
# for r in max_cnt_viewed:
#     print(r)
# for _ in range(2):
#     new_warrior_matrix = [[0 for _ in range(N)] for _ in range(N)]
#     for r in range(N):
#         for c in range(N):
#             if warrior_matrix[r][c] and max_cnt_viewed[r][c] != 2:
#                 print((r,c), "--------------------")
#                 m_cnt = warrior_move((r,c), (1,2), max_cnt_viewed, new_warrior_matrix)
#                 move_cnt += m_cnt
#     warrior_matrix = new_warrior_matrix
#
# attack_cnt = 0
# attack_cnt += warrior_matrix[1][2]
# print(move_cnt, attack_cnt)


routes = find_m_route((sr,sc), (er,ec))
# print(routes)
if routes == -1:
    print(-1)
else:
    for route in routes:
        stone_cnt, viewed = medusa_see(route)
        # for v in viewed:
        #     print(v)

        move_cnt = 0

        # 메두사가 도달한 칸에 있는 전사는 그냥 사라짐
        attack_cnt = 0
        warrior_matrix[route[0]][route[1]] = 0

        for i in range(2):

            new_warrior_matrix = [[0 for _ in range(N)] for _ in range(N)]
            for r in range(N):
                for c in range(N):
                    if warrior_matrix[r][c]:
                        if  viewed[r][c] != 2:
                            move_cnt += warrior_move(i, (r,c), route, viewed, new_warrior_matrix)
                        else:
                            new_warrior_matrix[r][c] += warrior_matrix[r][c]
            warrior_matrix = new_warrior_matrix

            # [구현 4]
            # 메두사와 같은 칸에 도달한 경우 전사는 메두사를 공격 후 사라짐
            attack_cnt += warrior_matrix[route[0]][route[1]]
            warrior_matrix[route[0]][route[1]] = 0

            # for w in warrior_matrix:
            #     print(w)

        print(move_cnt, stone_cnt, attack_cnt)

        # for r in viewed:
        #     print(*r)
    print(0)

