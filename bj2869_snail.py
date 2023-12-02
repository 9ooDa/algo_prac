# 답 화인해봄 (수식 세우기)

import sys

a, b, v = map(int, sys.stdin.readline().rstrip().split())
day = (v - b) / (a - b)

if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)