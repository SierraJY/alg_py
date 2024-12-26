import sys
import heapq

sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline())
card_sets = []
for _ in range(N):
    card_sets.append(int(sys.stdin.readline()))

heapq.heapify(card_sets)
cnt = 0

while len(card_sets) != 1:
    A = heapq.heappop(card_sets)
    B = heapq.heappop(card_sets)
    cnt += (A+B)
    heapq.heappush(card_sets, A+B)

print(cnt)


# what
# N개의 숫자 카드 묵음의 각각의 크기가 주어질 떄, 최소한 몇 번의 비교가 필요하지 구하라
# 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 비교(문제에서 그렇게 말함)

# how
# 우선 순위 큐(heap)
# 두 개 씩 Pop해서 합친다음 다시 Push

# 주의할 것
# Greedy 문제이기도 함
# 매 순간 가장 작은 두 카드 묶음을 선택해서 합치는 것이 최적해 보장
# (A+B) + (((A+B)) + C) + ((((A+B)) + C) + D) ... 인데
# 계속 더 해져있는 (A+B)와 같은 초기 합들이 작으면 작을 수록 전체 값이 작아지기 때문
# 따라서 작은 두 카드 묶음을 먼저 선택해서 합치는 것이 최적해를 보장함