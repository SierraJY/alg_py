import sys

sys.stdin = open(0, "r")
sys.stdin.readline()
for s in sys.stdin.readlines():
    splited = s.split()
    a = int(splited[0])
    b = int(splited[1])
    print(a+b)

# BOJ 채점 원리
# https://www.acmicpc.net/blog/view/55