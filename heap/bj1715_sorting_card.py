import sys
import heapq

n = int(sys.stdin.readline().rstrip())

res = []
h = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    heapq.heappush(h, num)

while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    heapq.heappush(h, a + b)
    heapq.heappush(res, a + b)
    
print(sum(res))