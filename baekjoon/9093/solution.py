// [문제 링크]: https://www.acmicpc.net/problem/9093

import sys
​
n = int(sys.stdin.readline().rstrip())
​
for _ in range(n):
    sen = sys.stdin.readline().rstrip().split()
​
    res = []
    
    for word in sen:
        flip = word[::-1]
        res.append(flip)
​
    print(' '.join(res))