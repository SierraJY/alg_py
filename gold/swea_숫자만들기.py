import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(r, opr_idx, term_result):
    global min_result, max_result

    if opr_idx == 0:
        term_result += nums[r]
    elif opr_idx == 1:
        term_result -= nums[r]
    elif opr_idx == 2:
        term_result *= nums[r]
    elif opr_idx == 3:
        term_result /= nums[r]
        term_result = int(term_result)

    if r == N-1 : #사용할 수 있는 최대 연산자의 개수
        min_result = min(min_result, term_result)
        max_result = max(max_result, term_result)
        return

    for i in range(4):
        if opr_cnt[i] != 0 :
            # 백트래킹으로 토클 처럼 껏다 키는 방법, 개수가 변화된 리스트를 계속 전달할 필요 없음
            opr_cnt[i] -= 1
            dfs(r+1, i, term_result)
            opr_cnt[i] += 1

T = int(input())

for t in range(T):
    min_result = 1e8
    max_result = -(1e8)

    N = int(input())
    opr_cnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    for i in range(4):
        if opr_cnt[i] != 0:
            opr_cnt[i] -= 1
            dfs(1, i, nums[0])
            opr_cnt[i] += 1

    print(f"#{t+1} {max_result-min_result}")

# opr_cnt를 visited 처럼 쓸 수 있지 않을까?
# opr_cnt를 백트래킹으로 되돌려 놓을 수 있지 않을까?
# 똑같은 연산자 2개 이상인 경우 프루닝 필요?