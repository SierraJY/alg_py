import sys

sys.stdin=open('input.txt', 'r')

N = int(sys.stdin.readline())
building_list = list(map(int, sys.stdin.readline().split()))

def line_equation(x, l, r):
    d = (building_list[r] - building_list[l]) / (r - l)

    return d * (x-l) + building_list[l]

max_view_cnt = 0

for flag in range(0,N):
    view_cnt = 0

    for compare in range(0, N):
        if flag == compare : continue
        compare_can_see = True
        left = min(flag, compare)
        right = max(flag, compare)

        for mid in range(left+1, right):
            if building_list[mid] >= line_equation(mid, left, right):
                compare_can_see = False
                break

        if compare_can_see :
            view_cnt += 1


        max_view_cnt = max(max_view_cnt, view_cnt)

print(max_view_cnt)


# what
# 가장 많은 빌딩이 보이는 빌딩 찾기

# how
# 직선의 방정식

# 주의할 것
# 단순 크기 비교로 푸는 문제가 아님
# 해당 문제에서 제시한 보인다는 기준에 유의할 것
# 즉, 어떤 건물에서 다른 건물을 볼 수 있는 조건이 수학적으로 어떻게 해석되느냐?

# 개선
# 각도(Slope)만 이용 가능
# 변수명 개선