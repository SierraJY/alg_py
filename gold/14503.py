import sys

sys.stdin = open('input.txt', 'r')

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
now_r, now_c, now_direction = map(int, sys.stdin.readline().split())
ROOM = [list(map(int, row.split())) for row in sys.stdin.readlines()]

cleaned_cnt = 0  # 청소횟수

while True:

    if ROOM[now_r][now_c] == 0:# 현재 위치 청소
        ROOM[now_r][now_c] = 'c'  # 청소된 곳은 'c'로 표시
        cleaned_cnt += 1

    can_clean = False  # 옮겨진 위치에서 청소가능 여부

    # 청소 실행은 위의 if문 코드에서함
    # 여기 코드부터는 청소기를 옮겨놓음
    for d in range(4):
        now_direction -= 1
        now_direction %= 4

        nr = now_r + DR[now_direction]
        nc = now_c + DC[now_direction]

        if (nr >= 1 and nc >= 1) and (nr < N - 1 and nc < M - 1) and ROOM[nr][nc] == 0:
            now_r, now_c = nr, nc
            can_clean = True
            break

    # 4방향 모두 청소가된 경우
    if can_clean == False:
        back_direction = now_direction - 2
        back_direction %= 4

        nr = now_r + DR[back_direction]
        nc = now_c + DC[back_direction]

        if ROOM[nr][nc] == 1:
            break

        else:
            now_r, now_c = nr, nc

print(cleaned_cnt)



# 무엇(기능)을 구현해야하는지 잘 파악해야함
# 청소, 회전(청소할 곳 선택), 이동
# 회전에 원형 배열 이용(나머지 연산자로 초과되는 회전 처리)

