# note : Max에 따라 Min 동시 갱신 하는 경우, 무작정 max(), min() 하면 안됨

import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

can_plays_list = [] #각 기타에 대하여 비트마스킹 연산으로 연주가능한 노래 목록을 리스트로 저장

for _ in range(N):
    g, m = input().split()
    can_plays = 0

    for i in range(M):
        if m[i] == 'Y':
            can_plays += 1 << M-i-1 # 노래 목록 인덱스는 0부터 시작하므로 -1 더 해줘야함

    can_plays_list.append(can_plays)

def count_play(can_plays): #십진수로 저장된 연주 가능 노래목록에 대하여 연주 가능한 노래 개수 반환
    cnt = 0

    for i in range(M):
        if can_plays & (1<<i):
            cnt += 1

    return cnt

max_can_play_cnt = 0
min_g_cnt = N
# dfs_cnt = 0 # 재귀 횟수 저장 == 경우의 수

def dfs(now_g, buy_g_cnt, now_can_play):
    global max_can_play_cnt, min_g_cnt #, dfs_cnt

    if now_g == N:
        #dfs_cnt += 1
        return

    dfs(now_g + 1, buy_g_cnt, now_can_play) #지금 now_g 노래를 포함하지 않는 경우

    if_buy_g_play_cnt = count_play(now_can_play | can_plays_list[now_g])
    if if_buy_g_play_cnt > max_can_play_cnt:
        max_can_play_cnt = if_buy_g_play_cnt
        min_g_cnt = buy_g_cnt + 1 #여기 min 사용하면 안됨!!
    elif if_buy_g_play_cnt == max_can_play_cnt:
        min_g_cnt = min(min_g_cnt, buy_g_cnt+1)

    dfs(now_g + 1, buy_g_cnt + 1, (now_can_play | can_plays_list[now_g])) #지금 now_g 노래를 포함하는 경우

dfs(0, 0, 0)

if max_can_play_cnt == 0:
    print(-1)
else:
    print(min_g_cnt)