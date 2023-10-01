n = int(input())
num = [int(input()) for _ in range(n)]

print(num)

def triangular_num(n):
    return (n*(n+1)) / 2

print(triangular_num(4))
print(triangular_num(5))
print(triangular_num(10))