n = int(input())

m = 60
s = 60

cnt = 0

for i in range(n+1):
    for j in range(m):
        for z in range(s):
            if '3' in str(i):
                cnt += 1
            elif '3' in str(j) or '3' in str(z):
                cnt += 1
print(cnt)