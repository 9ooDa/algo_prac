import sys

def gcd(x, y):
    new_x = y
    new_y = x % y
    if new_y == 0:
        return y
    return gcd(new_x, new_y)

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    tc = sorted(list(map(int, sys.stdin.readline().rstrip().split()))[1:], reverse=True)
    gcd_sum = 0
    for i in range(len(tc)-1):
        for j in range(i+1, len(tc)):
            gcd_sum += gcd(tc[i], tc[j])
    
    print(gcd_sum)