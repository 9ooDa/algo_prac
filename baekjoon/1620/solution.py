// [문제 링크]: https://www.acmicpc.net/problem/1620

import sys
​
n, m = map(int, sys.stdin.readline().rstrip().split())
pokemon = {}
rev_pokemon = {}
for i in range(n):
    x = sys.stdin.readline().rstrip()
    pokemon[x] = i+1
    rev_pokemon[i+1] = x
​
for _ in range(m):
    x = sys.stdin.readline().rstrip()
    if x.isdigit():
        print(rev_pokemon[int(x)])
    else:
        print(pokemon[x])