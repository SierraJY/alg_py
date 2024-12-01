import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    
    N, K = map(int, sys.stdin.readline().split())
    build_time = list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(N)]
    indegree = [0] * N  # 진입 차수 배열
    dp = [0] * N  # 각 건물을 짓는 데 걸리는 시간

    for _ in range(K):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1 - 1].append(v2 - 1)
        indegree[v2 - 1] += 1  # 진입 차수 증가

    W = int(sys.stdin.readline()) - 1  # 목표 건물 번호 (0부터 시작)

    # 위상 정렬을 위한 큐 초기화
    queue = deque()
    for i in range(N):
        if indegree[i] == 0:  # 진입 차수가 0인 노드 추가
            queue.append(i)
            dp[i] = build_time[i]  # 초기 시간 설정

    # 위상 정렬 수행
    while queue:
        current = queue.popleft()

        for next in graph[current]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[current] + build_time[next])  # 최소 시간 갱신

            if indegree[next] == 0:  # 진입 차수가 0이 되면 큐에 추가
                queue.append(next)

    print(dp[W])  # 목표 건물 W의 최소 시간 출력

# what
# 특정 건물을 지을 때까지 걸리는 최소시간

# how
# 위상정렬
# dp

# 잘못 풀었던 코드

# how
# 우선 W를 짓기위해 지어야할 건물들 파악해야하므로, W시작
# W에서 시작하는 BFS로 소요시간 더하기(?)
# 같은 레벨에 여러개의 건물이 있으면 최대소요시간인 것만(?)

# 주의할 것
# W에서 시작할 것이니 그래프 방향은 역으로 넣기
# 다음의 예시 : A 건물을 짓기 위해 지어야하는 B 건물에 A를 짓기위한 C가 같이 있는 경우(?)

# import sys
# from collections import deque
#
# sys.stdin=open('input.txt', 'r')
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     N, K = map(int, sys.stdin.readline().split())
#     build_time = list(map(int, sys.stdin.readline().split()))
#
#     graph = [[] for _ in range(N)]
#
#     for _ in range(K):
#         (v1, v2) = map(int, sys.stdin.readline().split())
#         graph[v2-1].append(v1-1)
#     #print(graph)
#
#     # 노드번호 0부터 사용
#     W = int(sys.stdin.readline()) - 1
#
#     total_time = build_time[W]
#
#     queue = deque()
#     queue.append(W)
#     visited = [0 for _ in range(N)]
#     visited[W] = 1
#
#     while queue:
#         now_level_cnt = len(queue)
#         next_level_max_time = 0
#
#         for _ in range(now_level_cnt):
#             popped = queue.popleft()
#
#             for v2 in graph[popped]:
#                 if visited[v2] == 0:
#                     visited[v2] = 1
#                     queue.append(v2)
#                     next_level_max_time = max(build_time[v2], next_level_max_time)
#
#         total_time += next_level_max_time
#
#     print(total_time)