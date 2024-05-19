n = 3
arr = [15, 27, 12]

idx_arr = [0] * (max(arr) + 1)

for num in arr:
    idx_arr[num] += 1

result = []
for i in range(len(idx_arr)-1, -1, -1): # 리스트에 기록된 정렬 정보 확인
    for j in range(idx_arr[i]):
        result.append(i)

print(result)