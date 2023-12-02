// [문제 링크]: https://www.acmicpc.net/problem/2869

import sys
​
a, b, v = map(int, sys.stdin.readline().rstrip().split())
day = (v - b) / (a - b)
​
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)