from collections import deque
from heapq import heapify, heappush, heappop


def solution(jobs):
    LEN = len(jobs)

    jobs.sort(key=lambda v: (v[0], v[1]))
    jobs = deque(jobs)
    waiting_heap = []

    finished = 0
    time = 0
    total_time = 0

    while finished != LEN:
        while jobs and jobs[0][0] <= time:
            poped = jobs.popleft()
            heappush(waiting_heap, (poped[1], poped[0]))

        if jobs and (not waiting_heap):
            poped = jobs.popleft()
            time = poped[0]
            heappush(waiting_heap, (poped[1], poped[0]))

        poped = heappop(waiting_heap)
        total_time += poped[0] + (time - poped[1])
        time += poped[0]
        finished += 1

    return total_time // LEN

print(solution([[0, 3], [1, 9], [2, 6]]))

# what
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법

# how
# 대기 시간이 짧아야 하는 것이 관건
# 현재 시점에서 처리할 수 있는 태스크들 끼리 소요 시간 비교해서 짧은 것 부터
# waiting_heap이 비어있고, 처리할 수 있는 태스크가 있으면 바로 처리
# 해당 태스크 처리 중에 요청들어오는 것들은 heap push
# waiting priority queue 사용 : (소요시간, 요청시간)으로 push함
# 현재 시간 저장 변수와 각 태스크의 총 소요시간을 저장하는 시간 관련 변수 2개 필요

# 주의사항
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리해야함
# 태스크를 처리하고 있는 중에도 새로운 태스크가 힙으로 들어올 수 있다!!!