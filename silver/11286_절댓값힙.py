import sys
import heapq

sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    ord = int(sys.stdin.readline())

    if ord == 0:
        if not heap: print('0')
        else:print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(ord), ord))





# what
# 주어진 횟수만큼 절댓값이 가장 작은 값(같으면 작은 수 부터)을 출력

# how
# 우선순위 큐(힙)