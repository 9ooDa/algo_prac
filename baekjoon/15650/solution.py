// [문제 링크]: https://www.acmicpc.net/problem/15650

import sys
​
n, m = map(int, sys.stdin.readline().rstrip().split())
​
ans = []
def back_track(idx):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(idx, n+1):
        ans.append(i)
        back_track(i + 1)
        ans.pop()
​
back_track(1)