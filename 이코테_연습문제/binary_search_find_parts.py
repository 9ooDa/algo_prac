from sys import stdin

n = int(input())
in_store = sorted(list(map(int, stdin.readline().rstrip().split())))
m = int(input())
request = list(map(int, stdin.readline().rstrip().split()))

print(in_store)
print(request)

def binary_search(arr, target, start, end):
    if start > end:
        return "no"
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return "yes"
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


for i in range(m):
    ans = binary_search(in_store, request[i], 0, n - 1)
    print(ans, end=' ')
