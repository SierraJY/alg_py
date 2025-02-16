import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
def dfs(now_pos, is_used_K, length):
    global max_length
    for d in range(4):
        nr = now_pos[0] + dr[d]
        nc = now_pos[1] + dc[d]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False:
            visited[nr][nc] = True
            if matrix[now_pos[0]][now_pos[1]] > matrix[nr][nc]:
                dfs((nr,nc), is_used_K, length+1)
            elif is_used_K == False and matrix[now_pos[0]][now_pos[1]] > (matrix[nr][nc] - K):
                next_origin = matrix[nr][nc]
                matrix[nr][nc] = matrix[now_pos[0]][now_pos[1]] - 1
                dfs((nr, nc), True, length+1)
                matrix[nr][nc] = next_origin
            visited[nr][nc] = False

    if length > max_length :
        max_length = length


T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    highest = 0
    for r in matrix:
        highest = max(max(r), highest)

    max_length = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == highest:
                visited = [[False for _ in range(N)] for _ in range(N)]
                visited[r][c] = True
                dfs((r,c), False, 1)

    print(f"#{t+1} {max_length}")



# 문제 & 알고리즘
# <가장 높은 봉우리 어떻게 찾음?>
# 입력 다 받고 찾아야함
# 입력 받으면서 찾으면 안됨

# <가장 긴 등산로 길이를 어떻게 알 수 있음?>
# 수학적으로 알 수 없음
# 가장 높은 봉우리에서 완전 탐색(dfs(재귀)) + 백트래킹
# dfs 시작 : 가장 높은 봉우리에서
# dfs 종료시에, 최대 등산로 길이를 갱신해야함, 재귀 시작점으로 값을 전달하면 안됨
# visited 필요, 각각의 등산로 시작에서 초기화 필요
# 못가는 곳이면 백트래킹으로 돌아와야함
# 백트래킹으로 원래 등산로 +K해줘야함!

# <등산로 깍기는?>
# dfs시 더 높거나 같은 높이 만났을 때 한번 깍아보기

# !!!!!주의!!!!
# <K만큼 깍을 수 있을 때 얼마나 깍아야 하는가?>
# 반드시 현재 위치의 봉우리 높이의 1만 깍아야함, 그래야 등산로 조건이 계속 유지됨(높이가 구불구불하면 안됨)

