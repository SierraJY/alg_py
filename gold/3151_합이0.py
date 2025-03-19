import sys

sys.stdin = open(0, 'r')
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

p_cnt = 0

for i in range(N-2):
    target = -(A[i])

    if A[i] > 0 : break

    l = i + 1
    r = N-1

    while l < r:

        lr_sum = A[l] + A[r]

        if lr_sum == target:
            if A[l] == A[r]:
                same = (r - l + 1)
                p_cnt += same*(same-1)//2
                break
            else:
                same_r = 1
                while A[r] == A[r-same_r]:
                    same_r += 1
                r -= same_r

                same_l = 1
                while A[l] == A[l +same_l]:
                    same_l += 1
                l += same_l

                p_cnt += ((same_r) * (same_l))


        elif lr_sum > target:
            r -= 1
        elif lr_sum < target:
            l += 1

print(p_cnt)

# 아이디어 & 알고리즘

# 3명의 합이 0이 되는 경우 찾기?
# => 완전 탐색 가능은 함
# N*3

# => 한 명 고정 후, 2명 이분탐색(?)
# 두 명의 합으로 -(나머지 한명)을 만들 수 있는 경우에 어떻게 처리? - 더 있을 수 있음

# => 두 명 선택 후 이분 탐색으로 동일 갯수 파악(?)
# 두 명은 어떻게 선택(?) - 조합..? (N : 10000만)
# 두 명 선택 투포인터(?)

# 동일 값이지만 다른 사람인 경우 있음
# => 재활용 가능?