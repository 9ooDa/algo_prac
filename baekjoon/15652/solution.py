// [문제 링크]: https://www.acmicpc.net/problem/15652

import sys
​
n, m = map(int, sys.stdin.readline().rstrip().split())
​
ans = []
​
def back_track(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
​
    for i in range(start, n+1):
        ans.append(i)
        back_track(i)
        ans.pop()
​
back_track(1)