# 숫자 카드 게임
n, m = map(int, input().split())
cards = []
for _ in range(n):
    cards.append(list(map(int, input().split())))

ans = 0
for row in cards:
    ans = max(min(row), ans)

print(ans)