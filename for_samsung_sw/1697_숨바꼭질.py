# note : 첫 level에 탐색을 종료해야하는 반례가 있는 경우

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())

visited = [False for _ in range(int(1e5)+1)]

from collections import deque

queue = deque()
queue.append(a)
visited[a] = True
now_level = 1
find_level = 0

if a == b:
    print(0)
    exit()

while queue:

    now_level_cnt = len(queue)

    for _ in range(now_level_cnt):
        popped = queue.popleft()

        for next in [popped-1, popped+1, popped*2]:
            if 0 <= next < int(1e5)+1 and visited[next] == False:
                if next == b:
                    find_level = now_level
                    break
                queue.append(next)
                visited[next] = True

        if find_level:
            break
    if find_level:
        break

    now_level += 1

print(now_level)

