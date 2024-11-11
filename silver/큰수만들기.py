def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return str(int("".join(numbers)))

# what
# 이어 붙여 만들 수 있는 가장 큰 수 알아내기

# how
# 숫자를 문자열화 한 다음 *3하여 비교
# 모든 숫자문자열을 3자리로 만든 후 비교함 (문제에서 최대 숫자가 1000이기 때문)
# [3, 30, 34]를 이어붙이기 위해 정렬한다면 [34, 3, 30]이 되어야함

# 주의할 것
# 반례 : [0,0,0,0] 과 같이 들어왔을 떄

# 알아야할 파이썬
# 문자열의 비교 : 문자열을 한 글자씩 왼쪽에서 오른쪽으로 비교
# 숫자문자열의 비교 : 숫자문자의 유니코드로 비교 ('100' < '45'가 True 임)