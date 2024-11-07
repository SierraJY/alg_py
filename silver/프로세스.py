from collections import deque

def solution(priorities, location):
    prs_queue = deque([enu for enu in enumerate(priorities)])

    ord = 1
    max_process = max(prs_queue, key=lambda x:x[1])[1]

    while prs_queue:
        if prs_queue[0][1] == max_process:
            if prs_queue[0][0] == location: return ord
            prs_queue.popleft()
            ord += 1
            max_process = max(prs_queue, key=lambda x: x[1])[1]
        else:
            prs_queue.append(prs_queue.popleft())

    return ord

print(solution([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

# what
# 특정 프로세스(locatioin)이 몇 번째로 실행되는지

# how
# 주어진 우선순위와 쌍으로 큐에 넣음
# 큐의 앞 부분 부터 가장 높은 순위가 맞는지 확인 후 popleft & 순서 += 1,
# popleft하려는 프로세스가 찾던 특정 프로세스면 바로 순서 return
# 높은 우선 순위가 아니면 popleft후 append

# 알아야할 파이썬
# max에도 key를 사용할 수 있다
# 이를 통해 튜플로 이루어진 배열을 활용할 수 있다
