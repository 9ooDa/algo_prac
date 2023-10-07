import sys

n = int(sys.stdin.readline().rstrip())

d = [5001] * (n + 5) # n < 5면 for loop에 인덱스 에러가 날 수 있기 때문에 +5

d[3] = 1
d[5] = 1

for i in range(6, n+1):
    d[i] = min(d[i - 3], d[i - 5]) + 1

print(d[n] if d[n] < 5001 else -1)
        
