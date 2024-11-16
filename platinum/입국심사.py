def solution(n, times):
    left = 1
    right = 1e9 * n

    min_required_time = max(times) * n

    while left <= right:

        mid = (right + left) // 2

        done = 0  # 심사가 끝난 사람 수

        """
        최소시간을 구해야하니까, 입국 심사관이 쉬지 않고 일한다고 가정
        각 심사관이 자신의 처리 시간으로 주어진 시간을 최대한 나누어 처리할 수 있는 인원을 합산함으로써, 해당 시간 내 처리 가능한 최대 인원을 계산
        처리한 최대인원이 n보다 같거나 크면 최소시간이 아닐 수 있음
        처리한 최대인원이 n보다 작으면 시간 부족
        """
        for t in times:
            done += mid // t

            if done >= n: break

        # >=인 이유 : 더 적게 걸리더라도 n명을 처리할 수 있는 시간이 있을 수 있음
        if done >= n:
            right = mid - 1
            min_required_time = min(min_required_time, mid)

        else:
            left = mid + 1

    return min_required_time

# what
# 모든 사람이 심사를 받는데 걸리는 최소 시간

# how
# 이분탐색
# 1. 가능한 시간 범위 상정 1 ~ (1e9 * n)
# 2. 해당 시간에 대하여 각 심사관이 처리하는 사람 수 총합 구하기
# 3. 해당 총합을 통해 범위 줄이기

# 주의할 것
# 가능한 시간 범위가 (가장 시간이 적게 걸리는 심사관 * n)이 아닌 이유 : 예시가 반례

# 알게된 것
# 이분탐색을 이렇게도 사용할 수 있구나

# 참고
# https://happy-obok.tistory.com/10