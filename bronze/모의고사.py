def solution(answers):
    FIR = (1, 2, 3, 4, 5)
    LEN_F = len(FIR)

    SEC = (2, 1, 2, 3, 2, 4, 2, 5)
    LEN_S = len(SEC)

    THR = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    LEN_T = len(THR)

    cor_cnts = [0, 0, 0]  # 각 학생 맞춘 갯수

    for n, a in enumerate(answers):
        if a == FIR[n % LEN_F]: cor_cnts[0] += 1
        if a == SEC[n % LEN_S]: cor_cnts[1] += 1
        if a == THR[n % LEN_T]: cor_cnts[2] += 1

    max_cor = max(cor_cnts)

    return [i + 1 for i in range(3) if cor_cnts[i] == max_cor]

# what
# 문제를 가장 많이 맞춘 사람 번호를 리스트에 담아서 반환(공동 존재)

# how
# 브루트 포스
# 각 학생이 찍는 번호 리스트는 순환 가능
# 각 학생이 맞춘 개수들을 저장하는 리스트 필요