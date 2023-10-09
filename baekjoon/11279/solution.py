// [문제 링크]: https://www.acmicpc.net/problem/11279

import heapq
import sys
​
n = int(sys.stdin.readline().rstrip())
h = []
​
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
​
    if num == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -num)