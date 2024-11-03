# 현수가 다니는 학교에는 동아리가 많이 있습니다.
# 현수가 다니는 학교의 학생은 1번부터 n번까지 번호가 부여된 n명의 학생들로 되어 있습니다
# 만약 1번 학생과 2번 학생이 같은 동아리 이면 [1,2]순서쌍으로 입력되며
# [2,3]은 3번 학생과 2번 학생이 같은 동아리입니다 즉 [1,2], [2,3]은 1,2,3번 학생이 같은 동아리를 의미합니다
# 모든 학생은 동아리를 가지고 있습니다
# 매개변수 n에 현수가 다니는 학교의 총 학생수가 주어지고 매개변수 edge에 학생들의 동아리
# 정보가 주어지면 현수가 다니는 학교의 동아리의 개수를 구하는 프로그램을 작성하세요.

def solution(n, edges):
    adj_list = [[] for _ in range(n+1)]

    for v_a, v_b in edges:
        adj_list[v_a].append(v_b)
        adj_list[v_b].append(v_a)

    visited = [0 for _ in range(n+1)]
    def dfs(stu):
        for same_club_stu in adj_list[stu]:
            if visited[same_club_stu] == 0:
                visited[same_club_stu] = 1
                dfs(same_club_stu)

    club_cnt = 0
    for s in range(1,n+1):
        if visited[s] == 0 :
            visited[s] = 1
            dfs(s)
            club_cnt += 1

    return club_cnt

print(solution(10, [[1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]]))
print(solution(20,
               [[1, 2], [2, 5], [5, 7], [9, 7], [5, 13], [15, 13], [3, 4], [4, 6], [6, 8], [8, 10], [11, 12], [14, 16],
                [16, 17], [17, 18], [19, 20]]))
print(solution(7, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(solution(30, [[5, 6], [6, 7]]))

# 주의할 점
# 1: 방향 그래프로 안됨
# A->B, C->B 는 하나의 연결로 취급되어야함
# 생각해보면 [6,8], [7,8]인 경우 위의 코드에서 동아리 2개로 취급됨
# 6,8번이 같은 동아리 7번 혼자 동아리
# 2: 마지막 출력 예시, 모든 학생은 동아리 하나는 가입되어있음

