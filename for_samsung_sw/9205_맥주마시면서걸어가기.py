# note : 처음에는 DFS 백트래킹이라고 생각했음
# note : 2차원 같지만 사실상 1차원임
# note: BFS에서는 각 노드에 처음 도달하는 순간이 가장 효율적인 경로로 도달한 순간이므로,
# 도달 가능성만 확인하면 되는 문제에서는 재방문을 고려할 필요가 없다.
# 즉, "갈 수 있냐 없냐"만 중요한 문제에서는 BFS로 한 번 방문한 곳은 다시 갈 이유가 없다

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

from collections import deque

for _ in range(T):
    n = int(input())
    house = tuple(map(int, input().split()))
    stores = []

    for _ in range(n):
        s = tuple(map(int, input().split()))
        stores.append(s)

    festival = tuple(map(int, input().split()))

    beer = 20
    queue = deque()
    queue.append(house)
    possible = False
    visited = [False for _ in range(n)]

    while queue:
        popped = queue.popleft()

        if distance(popped, festival) / 50 <= beer:
            possible = True
            break

        for s in range(n):
            if distance(popped, stores[s]) / 50 <= beer and visited[s] == False:
                visited[s] = True
                queue.append(stores[s])


    if possible:
        print('happy')
    else:
        print('sad')
