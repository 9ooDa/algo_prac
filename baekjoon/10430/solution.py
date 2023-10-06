// [문제 링크]: https://www.acmicpc.net/problem/10430

i, j, k = map(int, input().split())
​
print((i + j) % k)
print(((i % k) + (j % k)) % k)
print((i * j) % k)
print(((i % k) * j % k) % k)