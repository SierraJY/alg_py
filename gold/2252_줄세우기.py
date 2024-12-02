import sys
from collections import deque

sys.stdin = open("input.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N)]
in_degree = [0 for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1-1].append(v2-1)
    in_degree[v2-1] += 1

queue = deque()
for i in range(N):
    if in_degree[i] == 0:
        queue.append(i)

ord = []
while queue:
    popped = queue.popleft()
    ord.append(popped)

    for v2 in graph[popped]:
        in_degree[v2] -= 1
        if in_degree[v2] == 0:
            queue.append(v2)

print(" ".join(list(map(lambda x : str(x+1), ord))))


# what
# 일부 학생들의 키 비교를 통해 전체 줄 세우기
# 답은 여러가지가 있을 수 있음

# how
# 진입차수를 활용한 위상정렬

# 주의할 것
# 위의 문제에 대해서는 상관없지만
# 큐에 들어온 순서가 위상정렬 순서임
# 나간 순서가 아님

