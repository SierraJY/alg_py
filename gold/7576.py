import sys
from collections import deque

sys.stdin = open("../input.txt",'r')
col, row = list(map(int, sys.stdin.readline().split()))

# Python 에서는 스택과 큐를 따로 제공하지 않고, 둘을 합친 듯한 Deque를 제공함
riped_tomato_idx = deque()
tomato_box = []

for i in range(row):
    tomato_box.append(list(map(int,sys.stdin.readline().split())))

for i in range(row):
    for j in range(col):
        if tomato_box[i][j] == 1:
            riped_tomato_idx.append((i, j, 0)) #익은 날짜도 함께 저장하는 방식 사용

# 대각선 제외 위치 값 확인
# if문 4줄 작성하는 것보다 나은 방법
check_positions = [(1,0), (-1,0), (0,1), (0,-1)]

#모든 토마토가 모두 익는데 걸리는 예상 날짜
expected_days = 0

while len(riped_tomato_idx) != 0:
    riped_r, riped_c, riped_day = riped_tomato_idx.popleft()
    expected_days = max(expected_days, riped_day)

    for r, c in check_positions: #토마토 박스 범위를 벗어나서 익었는지 확인하지 않는지 반드시 확인
        if ((riped_r + r >= 0 and riped_c + c >= 0) and (riped_r + r < row and riped_c + c < col) and (tomato_box[riped_r + r][riped_c + c] == 0)):
            tomato_box[riped_r + r][riped_c + c] = 1
            riped_tomato_idx.append((riped_r + r, riped_c + c, riped_day+1))

# 절대 익을 수 없는 토마토가 있는지 확인
if any(0 in r for r in tomato_box):
    print(-1)
else:
    print(expected_days)