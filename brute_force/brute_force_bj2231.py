'''
분해합
'''
n = int(input())

ans = 0
for i in range(1, n):
    result = 0
    num = [int(x) for x in str(i)]

    if sum(num) + i == n:
        ans = i
        break

print(ans)