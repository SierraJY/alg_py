from collections import deque

def solution(maps):
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    r = len(maps)
    c = len(maps[0])
    visited = [[0 for _ in range(c)] for _ in range(r)]

    def bfs(pos):
        queue = deque()
        queue.append(pos)
        now_level = 0

        while queue:
            now_level += 1
            now_queue_cnt = len(queue)

            for _ in range(now_queue_cnt):
                poped = queue.popleft()

                for i in range(4):
                    nr = poped[0] + dr[i]
                    nc = poped[1] + dc[i]

                    if 0 <= nr < r and 0 <= nc < c and maps[nr][nc] == 1 and visited[nr][nc] == 0:
                        if nr == (r - 1) and nc == (c - 1): return now_level + 1
                        visited[nr][nc] = 1
                        queue.append((nr, nc))

        return -1

    return bfs((0, 0))

# what
# 상대 진영에 도달하는 최소 칸의 개수

# how
# 시뮬레이션(방향 벡터)
# 최단 거리이므로 BFS
# 2차원 visited 리스트를 사용

# 주의할 것
# visited가 반드시 필요함, 도달할 수 없는 경우에 무한 루프가 발생
# 큐에 넣기 직전에 visited 체크를 해야 queue에 중복으로 넣지 않음