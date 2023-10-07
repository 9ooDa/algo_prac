from sys import stdin

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        wires = [x // mid for x in arr]
        # print("mid", mid)
        # print("wires", wires)
        # print("sum wires", sum(wires))

        if sum(wires) < target:
            end = mid - 1
        else:
            start = mid + 1
    # 최댓값을 찾아야해서
    return end

k, n = map(int, stdin.readline().rstrip().split())
array = []

for _ in range(k):
    array.append(int(stdin.readline().rstrip()))
# 랜선의 길이는 0이 될 수 없어서 start=1
print(binary_search(sorted(array), n, 1, max(array)))