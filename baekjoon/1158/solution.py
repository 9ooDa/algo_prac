// [문제 링크]: https://www.acmicpc.net/problem/1158

import sys
from collections import deque
​
n, k = map(int, sys.stdin.readline().rstrip().split())
arr = deque([i+1 for i in range(n)])
res = []
​
while arr:
    for _ in range(k - 1):
        arr.append(arr.popleft())
​
    res.append(arr.popleft())
​
print(str(res).replace('[', '<').replace(']', '>'))