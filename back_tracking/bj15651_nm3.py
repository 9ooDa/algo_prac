import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

ans = []
def back_track():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(1, n+1):
        ans.append(i)
        back_track()
        ans.pop()

back_track()