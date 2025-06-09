# note : 경로의 수를 세는 BFS ≠ 일반적인 최단거리 BFS
#
# 일반 BFS: 방문한 노드는 다시 방문하지 않음 (visited[node] = True)
# 경로 수 BFS: 같은 레벨에서는 여러 경로로 같은 노드에 도달 가능
#
# 방문 처리의 타이밍 차이
# 일반 BFS: 큐에 넣을 때 즉시 visited = True
# 경로 수 BFS: 레벨이 끝난 후 방문 경로 수 처리

# note 1 : 만약 찾은 경로가 최소 레벨일 때, 중간에 특정 노드에 여러 번 도달하게 되는 경우가 있다면, 도달하는 타이밍은 모두 같은 레벨에서 이루어질 것이다.

# note 2: 어떤 노드든 최단거리로 도달하는 모든 경로는 정확히 같은 레벨에서 발생
# 나중 레벨에서 같은 노드에 도달하는 것은 더 긴 경로이므로 최단경로가 아님
# 따라서 경로 수를 셀 때는 각 노드의 최초 도달 레벨에서만 경로 수를 누적하면 됨

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())

visited_cnt = [0 for _ in range(int(1e5)+1)]

from collections import deque

queue = deque()
queue.append(a)
visited_cnt[a] = 1
now_level = 1
find_level = 0
find_level_cnt = 0

if a == b:
    print(0)
    print(1)
    exit()

while queue:

    now_level_cnt = len(queue)
    # 다음 레벨 노드별로 경로 수를 누적
    next_level_cnt = {}

    for _ in range(now_level_cnt):
        popped = queue.popleft()

        for next in [popped - 1, popped + 1, popped * 2]:
            if 0 <= next < int(1e5) + 1:
                if next == b:
                    find_level = now_level
                    find_level_cnt += visited_cnt[popped]
                else:
                    if next not in next_level_cnt:
                        next_level_cnt[next] = 0
                    next_level_cnt[next] += visited_cnt[popped]

    # 다음 레벨 처리
    for next, cnt in next_level_cnt.items():
        if visited_cnt[next] == 0:  # 처음 방문하는 노드만 큐에 추가
            queue.append(next)
        visited_cnt[next] = cnt

    if find_level:
        break

    now_level += 1

print(find_level)
print(find_level_cnt)