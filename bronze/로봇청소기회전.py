def solution(moves):

    now_position = [0, 0]
    now_direction = 1

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    for c in moves:
        if c == 'G':
            nr = now_position[0] + dr[now_direction]
            nc = now_position[1] + dc[now_direction]
            if (nr>=0 and nc >=0) and (nc<100 and nc <100):
                now_position[0],now_position[1] = nr, nc
        elif c == 'R':
            now_direction += 1
            now_direction %= 4 # 초과되는 회전 처리
        elif c == 'L':
            now_direction -= 1
            now_direction %= 4 # 초과되는 회전 처리
            #파이썬의 음수 나머지 처리 참고
            #이것도 가능, 위에는 파이썬만 가능
            # now_direction += 3
            # now_direction %= 4  # 초과되는 회전 처리

    return now_position

print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
