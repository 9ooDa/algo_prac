// [문제 링크]: https://www.acmicpc.net/problem/1182

n, s = map(int, input().split())
perm = list(map(int, input().split()))
​
count = 0
def back_track(idx, res):
    global count
    if idx >= n:
        return
    
    res += perm[idx]
    if res == s:
        count += 1
    
    back_track(idx + 1, res - perm[idx])
    back_track(idx + 1, res)
​
back_track(0, 0)
print(count)