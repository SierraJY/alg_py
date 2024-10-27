def solution(box, limit):

    box.sort(key = lambda b : -b[1])

    apple_cnt = 0
    for b_n, a_n in box:

        tmp_n = min(limit, b_n) # min으로 간단하게 처리
        limit -= tmp_n
        apple_cnt += tmp_n * a_n

        if limit == 0: break

    return apple_cnt

print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))

# what
# 실을 수 있는 사과의 최대 개수

# how
# 많은 사과를 담고 있는 박스 부터(그리디)

# condition
# 박스 종류에 따라 담겨있는 사과의 개수 다름
# 최대 박스의 개수 제한 있음
