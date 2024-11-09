import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    cooking = 0
    while scoville[0] < K:
        if len(scoville) == 1: return -1
        cooking += 1
        poped_1 = heapq.heappop(scoville)
        poped_2 = heapq.heappop(scoville)
        heapq.heappush(scoville, poped_1 + poped_2 * 2)

    return cooking

# what
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수

# how
# 우선순위 큐(최소 힙)
