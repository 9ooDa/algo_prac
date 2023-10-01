nanjaeng = [int(input()) for _ in range(9)]

answer = False
total = sum(nanjaeng)
for i in range(8):
    for j in range(i+1, 9):
        if (total - nanjaeng[i] - nanjaeng[j]) == 100:
            nanjaeng.pop(j)
            nanjaeng.pop(i)
            answer = True
            break
    if answer == True:
        break

for x in sorted(nanjaeng):
    print(x)