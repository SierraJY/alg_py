def solution(n, moves):

    position = [0,0]

    # 상수들은 튜플로 저장해두는 것이 좋다
    directions = ('U', 'R', 'D', 'L')
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    for c in moves:
        now_direction = directions.index(c)

        nr = position[0] + dr[now_direction]
        nc = position[1] + dc[now_direction]

        if (nr>=0 and nc>=0) and (nr<n and nc<n):
            position[0],position[1] = nr, nc

    return position

print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))
