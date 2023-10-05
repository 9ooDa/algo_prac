// [문제 링크]: https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())
ans = []
def back_track():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            back_track()
            ans.pop()
​
back_track()