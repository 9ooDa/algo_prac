// [문제 링크]: https://www.acmicpc.net/problem/1764

n, m = map(int, input().split())
notheard = {}
notseen = []
for _ in range(n):
    notheard[input()] = False
​
for _ in range(m):
    notseen.append(input())
​
count = 0
for s in notseen:
    if s in notheard.keys():
        count += 1
        notheard[s] = True
​
print(count)
for k, v in sorted(notheard.items()):
    if v == True:
        print(k)