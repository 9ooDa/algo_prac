from sys import stdin

def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)
    

n = int(stdin.readline().rstrip())
a = sorted(list(map(int, stdin.readline().rstrip().split())))
m = int(stdin.readline().rstrip())
m_list = list(map(int, stdin.readline().rstrip().split()))

for i in range(m):
    if binary_search(a, m_list[i], 0, n-1) != None:
        print(1)
    else:
        print(0)
