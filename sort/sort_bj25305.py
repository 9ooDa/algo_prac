n, k = map(int, input().split())

scores = list(map(int, input().split()))
count = [0] * (max(scores)+1)
cutline = []

for i in range(len(scores)):
    count[scores[i]] += 1

for i in range(len(count)-1, -1, -1):
    for j in range(count[i]):
        cutline.append(i)

print(cutline[k-1])