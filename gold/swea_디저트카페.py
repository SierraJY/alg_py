import sys

sys.stdin= open("sample_input.txt", 'r')
input = sys.stdin.readline

T = int(input())

directions = ((1,1), (1,-1), (-1,-1), (-1,1))

def move_n_dfs(now_pos, now_dir, d_cnt):
    """
    now_pos : 현재 위치
    now_dir : 현재 바라보는 방향
    d_cnt : 들린 카페 개수
    """
    nr = now_pos[0] + directions[now_dir][0]
    nc = now_pos[1] + directions[now_dir][1]

    if 0 <= nr < N and 0 <= nc < N and toggle[matrix[nr][nc]] != True:
        toggle[matrix[nr][nc]] = True
        dfs((nr, nc), now_dir, d_cnt)
        toggle[matrix[nr][nc]] = False

def dfs(now_pos, now_dir, d_cnt):
    global max_desert

    if now_dir == 3 :
        if now_pos == start:
            if max_desert < d_cnt :
                max_desert = d_cnt
            return

    elif now_dir == 2:
        if (now_pos[0], now_pos[1]) == (start[1], start[0]):
            move_n_dfs(now_pos, now_dir+1, d_cnt + 1)
            return
        # 방향 2인 상태로 올라가면서 start[0]과 행 위치가 같아지는 순간부터는 고려안해도됨
        if now_pos[0] <= start[0] : return

    move_n_dfs(now_pos, now_dir, d_cnt + 1) #원래 가던 방향으로
    if (now_dir == 0 and now_pos == start) or now_dir == 3: #꺽을 수 없는 경우들
        return
    move_n_dfs(now_pos, now_dir+1, d_cnt + 1) #꺽은 방향으로


for t in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    toggle = [False for _ in range(101)]
    max_desert = -1

    for r in range(0, N-1): #꺽는 방향을 정해두었으므로, 절대 돌아올 수 없는 지점들이 있음, 그 지점들을 거름
        for c in range(1, N - 1):
            start = (r,c)
            dfs(start, 0, 0)

    print(f"#{t+1} {max_desert}")


# 알고리즘 & 기법
# <dfs>
# 경로 끝까지 가보면서 제약에 걸리는 루트인지 확인해야함
# 시작방식 : dfs시작 지점은 정해져있으니까, 다음 dfs호출하면서 디저트 개수를 더함
# 종료조건 : 현재 방향 순서가 3이고 원래 지점 돌아왔을 떄
# <백트래킹>
# 제약에 걸리면 다시 돌아가서 다음 경로 탐색
# 디저트 개수별로 toggle 리스트 선언
# 프루닝 : 방향2인 상태에서는 꺽는 조건이 정해짐
# 프루닝 : 방향 2인 상태에서 r이 start의 r보다 같거나 더 위로 가는 경우
# <구현>
# 대각선 방향으로만 이동이 가능함
# 꺽는 순서 결정 (하,우) -> (하,좌) -> (상,좌) -> (우,상)
# 미리 확인 가능한 시작점 제한 : 위와 같이 꺽는다고 결정하면 탐색 안해도 되는 지점이 있음
