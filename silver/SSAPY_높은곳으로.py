import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    N, P = list(map(int, sys.stdin.readline().split()))

    choices = [i for i in range(1,N+1)]
    for i in range(1, len(choices)+1):
        if sum(choices[0:i]) == P :
            choices.pop(0)

    print(sum(choices))


# what
# 올라갈 수 있는 가장 높은 층

# how
# 다 올라갔다고 가정

# 주의할 것
# 그냥 현재 층에서 i를 더해서 P일 땐, 선택안한다고 하면
# 반례 생김  (10 55 : 답 54)