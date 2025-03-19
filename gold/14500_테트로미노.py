import sys

sys.stdin = open(0, 'r')
input = sys.stdin.readline

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def dfs(r,c, now_cnt, now_sum):
    global max_sum

    # 가지치기
    if now_sum + (4 - now_cnt) * matrix_max <= max_sum:  # 나머지 블럭이 모두 최댓값이어도 현재 ans 값보다 작다면 dfs 순회 정지
        return

    if now_cnt == 4:
        max_sum = max(max_sum, now_sum)
        return

    visited[r][c] = True
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            dfs(nr, nc, now_cnt+1, now_sum+matrix[r][c])
    visited[r][c] = False

def fuckyou_sum(r, c, center):
    global max_sum

    for d in range(4):
        in_range = 0
        now_sum = center
        for i in range(3):
            dd = (d+i) % 4
            nr = r + dr[dd]
            nc = c + dc[dd]
            if 0 <= nr < N and 0 <= nc < M:
                in_range += 1
                now_sum += matrix[nr][nc]

        if in_range == 3:
            max_sum = max(max_sum, now_sum)

N, M = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

matrix_max = max(map(max, matrix))

max_sum = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
for r in range(N):
    for c in range(M):
        dfs(r, c, 0, 0)
        fuckyou_sum(r,c,matrix[r][c])

print(max_sum)

# 아이디어 & 알고리즘
# 도형 놓기?
# => 구현
# => dict에 도형 모형 저장
# => 도형 놓는 곳은 항상 최좌상

# 회전 , 대칭 어떻게?
# => 매트릭스를 회전?
# => 도형을 회전?
    # 회전 -> 대칭 == 대칭 -> 회전
    # one은 90도 회전 1번만 해도됨
    # two는 모두 동일
    # three는 회전, 대칭에 따라 모두 다름
    # four는 90도 회전 1번과 & 대칭
    # five는 회전만 3번만 해도 됨
# 이 방식이면 둘다 시간 초과이거나 너무 복잡

# => 3번만 움직이면 다 갈 수 있는 도형들
    # 법규 모양 어떻게...?
    # => 3번 움직여서 갈 수 있는 모양이 아님


# 가지치기?