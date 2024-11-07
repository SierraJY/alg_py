from collections import deque

def solution(progresses, speeds):
    answer = []
    prg_queue = deque(progresses)
    spd_queue = deque(speeds)

    while prg_queue:
        cnt = 0

        for i in range(len(prg_queue)): prg_queue[i] += spd_queue[i]

        while prg_queue and prg_queue[0] >= 100 : #prg_queue가 비었는지 확인부터
            prg_queue.popleft()
            spd_queue.popleft()
            cnt += 1

        if cnt > 0: answer.append(cnt)

    return answer

# what
# 각 배포마다 몇 개의 기능이 배포되는지

# how
# 큐 사용
# 일단 다 큐에 넣어둠
# 앞의 요소가 다 되었는지 확인 후 popleft, 뒤에 요소들도 popleft

# 주의할 것
# 항상 인덱스를 이용한 비교를 조건문에서 수행할 때는, 큐나 스택이 비었는지 확인부터해야함