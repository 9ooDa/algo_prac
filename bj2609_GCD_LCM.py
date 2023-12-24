import sys

def GCD(x, y):
    if x % y == 0:
        return y
    new_x = y
    new_y = x % y
    return GCD(new_x, new_y)

def LCM(x, y):
    return (x * y) // GCD(x, y)

a, b = map(int, sys.stdin.readline().rstrip().split())
print(GCD(a, b))
print(LCM(a, b))