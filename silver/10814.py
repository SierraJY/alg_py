import sys

sys.stdin = open("input.txt", 'r')

N = int(sys.stdin.readline())

for age, name in sorted([[int(m[0]), m[1]]for m in [m.split() for m in sys.stdin.readlines()]], key = lambda m : m[0]):
    print(age, name)

# how
# sorted의 Key 인자에 lambda를 이용한 정렬
# 리스트 컴프리헨션을 활용한 숏 코딩