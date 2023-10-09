// [문제 링크]: https://www.acmicpc.net/problem/10814

import sys
import heapq
​
n = int(sys.stdin.readline().rstrip())
h = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().rstrip().split())
    heapq.heappush(h, (int(age), i, name))
​
h = sorted(h, key = lambda x: (x[0], x[1]))
​
for person in h:
    print(person[0], person[2])
​