// [문제 링크]: https://www.acmicpc.net/problem/11286

import heapq
import sys
​
n = int(sys.stdin.readline().rstrip())
pos = []
neg = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
​
    if num == 0:
        if len(pos) == 0 and len(neg) == 0:
            print(0)
        elif len(pos) == 0:
            print(-heapq.heappop(neg))
        elif len(neg) == 0:
            print(heapq.heappop(pos))
        else:
            if abs(pos[0]) == abs(neg[0]):
                print(-heapq.heappop(neg))
            elif abs(pos[0]) > abs(neg[0]):
                print(-heapq.heappop(neg))
            elif abs(pos[0]) < abs(neg[0]):
                print(heapq.heappop(pos))
    else:
        if num > 0:
            heapq.heappush(pos, num)
        elif num < 0:
            heapq.heappush(neg, -num)