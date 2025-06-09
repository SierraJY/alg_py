import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

from collections import deque

visited = [False for _ in range(F+1)]
queue = deque()
queue.append(S)
visited[S] = True
now_level = 1
find_level = 0

if S == G:
    print(0)
    exit()

while queue:
    now_level_cnt = len(queue)

    for _ in range(now_level_cnt):
        popped = queue.popleft()

        for next in [popped+U, popped-D]:
            if 1 <= next < F+1 and visited[next] == False:
                if next == G:
                    find_level = now_level
                    break
                visited[next] = True
                queue.append(next)

        if next == G:
            break

    if next == G:
        break

    now_level += 1

if not find_level:
    print('use the stairs')
else:
    print(now_level)