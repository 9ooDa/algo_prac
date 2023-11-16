// [문제 링크]: https://www.acmicpc.net/problem/1712

import sys
​
fix, var, price = map(int, sys.stdin.readline().rstrip().split())
​
cost = fix
benefit = 0
cnt = cost // price
​
if var >= price:
    print(-1)
else:
    print(fix // (price - var) + 1)