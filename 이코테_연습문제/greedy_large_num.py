# 큰 수의 법칙
ans = 0
cnt = 0

n, m, k = map(int, input().split())
num_list = sorted(list(map(int, input().split())), reverse=True)

while True:
    for _ in range(k):
        if cnt == m:
            break
        ans += num_list[0]
        cnt += 1
    if cnt == m:
        break
    ans += num_list[1]
    cnt += 1

print(ans)