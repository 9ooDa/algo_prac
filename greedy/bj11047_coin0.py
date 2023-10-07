'''
통과
'''
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse=True)

count = 0
while k > 0:
    for c in coins:
        if k // c >= 1:
            count += k // c
            used = c * (k // c)
            k -= used

print(count)