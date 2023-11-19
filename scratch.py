import sys

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total_b = sum([mid if mid < x else x for x in arr])
        
        if total_b > target:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    
    return mid
    
n = int(sys.stdin.readline().rstrip())
b = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
total = int(sys.stdin.readline().rstrip())

print(binary_search(b, total, 0, max(b)))
