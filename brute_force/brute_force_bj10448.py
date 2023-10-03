'''
유레카 이론
'''
def triangular_num(n):
    return (n*(n+1)) // 2

Tn = 0
k = 1
while Tn <= 1000:
    Tn = triangular_num(k)
    k += 1

def find_eureka(num):
    for x in range(1, k+1):
        for y in range(1, k+1):
            for z in range(1, k+1):
                eureka = triangular_num(x) + triangular_num(y) + triangular_num(z)
                if eureka == num:
                    return 1
    return 0

n = int(input())
num_list = [int(input()) for _ in range(n)]

for x in num_list:
    print(find_eureka(x))