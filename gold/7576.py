import sys
from collections import deque

sys.stdin = open("input.txt",'r')
col, row = list(map(int, sys.stdin.readline().split()))

# Python 에서는 스택과 큐를 따로 제공하지 않고, 둘을 합친 듯한 Deque를 제공함
riped_tomato_idx = deque()
tomato_box = []

for i in range(row):
    tomato_box.append(list(map(int,sys.stdin.readline().split())))

for i in range(row):
    for j in range(col):
        if tomato_box[i][j] == 1:
            riped_tomato_idx.append((i, j))

# 간략한 대가선 제외 위치 값 확인하기
# 아니면 if문 4줄 작성해야함
check_positions = [(1,0), (-1,0), (0,1), (0,-1)]
expected_days = 0

while len(riped_tomato_idx) != 0:
    expected_days += 1
    expected_riped_tomato_idx = []

    while len(riped_tomato_idx) != 0:
        riped_r, riped_c = riped_tomato_idx.popleft()
        for r, c in check_positions:
            if (riped_r + r >= 0 and riped_c + c >= 0) and (riped_r + r < row and riped_c + c < col):
                if tomato_box[riped_r + r][riped_c + c] == 0:
                    tomato_box[riped_r + r][riped_c + c] = 1
                    expected_riped_tomato_idx.append((riped_r + r, riped_c + c))

    riped_tomato_idx.extend(expected_riped_tomato_idx)

# 절대 익을 수 없는 토마토가 있는지 확인
for i in range(row):
    for j in range(col):
        if tomato_box[i][j] == 0:
            expected_days = 0

print(expected_days-1)