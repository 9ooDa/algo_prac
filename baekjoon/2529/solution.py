// [문제 링크]: https://www.acmicpc.net/problem/2529

import sys
​
k = int(sys.stdin.readline().rstrip())
comparison = list(map(str, sys.stdin.readline().rstrip().split()))
​
visited = [0] * 10
max_ans = ''
min_ans = ''
​
def check(i, j, c):
    if c == '>':
        return i > j
    else:
        return i < j
    
def back_track(idx, res):
    global max_ans, min_ans
​
    if idx == k + 1:
        if len(min_ans) == 0:
            min_ans = res
        else:
            max_ans = res
        return
​
    for i in range(10):
        if visited[i] == 0:
            if idx == 0 or check(res[-1], str(i), comparison[idx-1]):
                visited[i] = True
                back_track(idx + 1, res + str(i))
                visited[i] = False
​
​
back_track(0, "")
print(max_ans)
print(min_ans)