import sys
from collections import deque

sys.stdin = open(0, 'r')
N, K = map(int, sys.stdin.readline().split())

def bfs():
    queue = deque()
    queue.append(N)
    visited = [0 for _ in range(int(1e5+1))]
    dp = [0 for _ in range(int(1e5+1))]

    while queue:
        X = queue.popleft()

        if X == K:
            print(dp[X])
            return

        if 0 <= 2*X < len(visited) and visited[2*X] == 0:
            visited[2*X] = 1
            dp[2*X] = dp[X]
            queue.appendleft(2*X)

        if 0 <= X-1 < len(visited) and visited[X-1] == 0:
            visited[X-1] = 1
            dp[X-1] = dp[X]+1
            queue.append(X-1)

        if 0 <= X+1 < len(visited) and visited[X+1] == 0:
            visited[X+1] = 1
            dp[X+1] = dp[X]+1
            queue.append(X+1)

bfs()

# 알게된 것
# 이 문제의 복잡한 로직을 외우려고 하기 보다
# 그래프가 직접적으로 주어지지 않더라도, 머릿 속으로 그래프를 그려볼 수 있어야함

# what
# 수빈이가 동생을 찾는 최단 시간
# 걷기는 1초 걸림, 이동위치 : X+1, X-1
# 순간이동은 0초 걸림, 이동위치 : 2*X

# how
# BFS

# (BFS로 풀 때) 주의할 것
# 1
# 비슷한 류의 BFS 문제들은 모두 간선의 가중치가 1이라고 가정하지만
# 이 문제는 가선의 가중치가 다르다고 볼 수 있음

# 2
# 순간이동 -> -1 -> +1 순서로 고려해야함
# EX )
# 3->6->5->10 (-1을 먼저 한 경우)
# 3->6->7->14 or 3->6->7->8->9->10(+1을 먼저 한 경우)
