def solution(numbers, target):
    LEN = len(numbers)

    def dfs(now_sum, idx):
        if idx == LEN - 1:  # 모든 숫자를 사용했고
            if now_sum == target:  # 원하는 합에 도달했을 때
                return 1
            else:
                return 0

        return dfs(now_sum + numbers[idx + 1], idx + 1) + dfs(now_sum - numbers[idx + 1], idx + 1)

    return dfs(numbers[0], 0) + dfs(-numbers[0], 0)

# what
# target을 만들 수 있는 경우의 수
# numbers의 순서는 바꿀 수 없고 반드시 다 사용해야함

# how
# dfs(numbers[0], 0)
# dfs(-numbers[0], 0)
# 최소 개수 등을 구하는게 아니고, 모든 경우의 수에 다 도달해봐야하니까 dfs문제가 아닐까 예상함
# 1. DFS(깊이 우선 탐색)를 사용하여 모든 가능한 조합을 탐색
# 2. 각 숫자마다 더하거나 빼는 두 가지 경우를 재귀적으로 탐색
# 3. 마지막 숫자까지 도달했을 때, 합계가 target과 일치하면 유효한 경우로 카운트
# 시간 복잡도: O(2^n), 여기서 n은 numbers 배열의 길이
# 각 숫자마다 2가지 선택(더하기 또는 빼기)이 있으므로, 총 2^n개의 경우의 수를 탐색

# 스택으로도 가능할 것 같음

# 알게된 것
# 노드 엣지로 구성된 그래프를 그릴 수 있는 상하좌우, map 문제 뿐 아니라 이런 것도 bfs/dfs 문제임을 깨닫게 해준 문제
# 이진 트리 형식으로 뻗어나갈 수 있는 문제는 dfs/bfs로 접근할 수 있음을 항상 염두