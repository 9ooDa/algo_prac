n = int(input())
num_li = []
for _ in range(n):
    num_li.append(int(input()))

for i in range(n-1, 0, -1):
    swapped = False
    for j in range(i):
        if num_li[j] > num_li[j+1]:
            num_li[j], num_li[j+1] = num_li[j+1], num_li[j]
            swapped = True
    if not swapped:
        break

for i in range(n):
    print(num_li[i])
