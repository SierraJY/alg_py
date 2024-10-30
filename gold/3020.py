import sys
from bisect import bisect_left

# N : 동굴 길이
# H : 동굴 높이
sys.stdin = open('input.txt', 'r')
N, H = list(map(int, sys.stdin.readline().split()))

up_bar = [] #석순
down_bar = [] #종유석
for i in range(N):
    if i % 2 != 0 : up_bar.append(int(sys.stdin.readline()))
    else : down_bar.append(int(sys.stdin.readline()))

up_bar.sort()
down_bar.sort()

min_destroy_cnt = N
min_destroy_roots_cnt = 0

for r in range(H):
    root = r+ 0.5
    destroy_cnt = 0

    up_bar_minimum = bisect_left(up_bar, root) if bisect_left(up_bar, root) != len(up_bar) else len(up_bar) # 안 부셔지는 개수
    down_bar_minimum = bisect_left(down_bar, H-root) if bisect_left(down_bar, H-root) != len(down_bar) else len(down_bar) # 안 부셔지는 개수
    destroy_cnt += (len(up_bar) - up_bar_minimum) + (len(down_bar) - down_bar_minimum)

    if min_destroy_cnt > destroy_cnt :
        min_destroy_cnt = destroy_cnt
        min_destroy_roots_cnt = 1

    elif min_destroy_cnt == destroy_cnt :
        min_destroy_roots_cnt += 1

print(min_destroy_cnt, min_destroy_roots_cnt)

# what
# 파괴해야할 장애물의 최솟값과 그러한 구간이 총 몇개

# how
# 장애물 순서는 중요 X
# 각 구간의 높이에서 석순과 종유석 각각에 대하여 '이분탐색'으로 안 부셔지는 개수 확인
# 안 부셔진 개수로 부순 개수 확인
# 석순과 종유석 부순 개수 계산

# 주의할 것
# 구간의 실제 높이값은 구간 + 0.5   (0구간의 높이는 0.5)
# 종유석일 때 어떻게 높이를 수정해야하는지 생각
