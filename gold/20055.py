import sys
from collections import deque

sys.stdin = open(0, 'r')
input = sys.stdin.readline


N, K = map(int, input().split())
belts = deque(map(int, input().split()))
rbt_pos = deque()

zero_cnt = 0
result = 0

while zero_cnt < K:

    result += 1

    belts.appendleft(belts.pop()) # 벨트 한 칸 씩 이동

    if rbt_pos: # 벨트위에 로봇이 있을 때

        if rbt_pos[-1] == N-2: # 벨트 한 칸 씩 이동했을 때, 내리는 곳 도달하는 로봇 내리기
            rbt_pos.pop()

        for i in range(len(rbt_pos)-1, -1, -1): # 로봇 움직이기
            rbt_pos[i] += 1 # 벨트 이동하면서 로봇 위치 갱신
            next_pos = rbt_pos[i] + 1 # 로봇이 직접 움직일 수 있다면 한 칸 더 이동
            if belts[next_pos] > 0 and next_pos not in rbt_pos:
                belts[next_pos] -= 1
                rbt_pos[i] += 1

                if belts[next_pos] == 0 :
                    zero_cnt += 1

                    if zero_cnt == K:
                        break

            if rbt_pos and rbt_pos[-1] == N - 1:
                rbt_pos.pop()

    if zero_cnt == K:
        break

    if belts[0] > 0:
        rbt_pos.appendleft(0)
        belts[0] -= 1
        if belts[0] == 0:
            zero_cnt += 1

print(result)

# 아이디어 & 알고리즘
# 컨베이어 벨트 구현 어떻게?
# =>리스트 1개 활용? (Deque)
# =>벨트 회전에 append, pop 활용
# => 내구도 0인 칸 K개 이상되기 까지 while문

# 벨트 위에서 로봇 이동 구현 어떻게?
# => robot 위치를 저장하는 다른 리스트

# 파이썬 알게된 것
# rotate 메서드