from sys import stdin

def binary_search(arr, target):
    start, end = 0, max(budget_list)
    while start <= end:
        ceiling = (start+end) // 2
        total = sum([ceiling if x > ceiling else x for x in arr])

        if total > target:
            end = ceiling - 1
        else:
            result = ceiling
            start = ceiling + 1
    
    return result


n = int(stdin.readline().rstrip())
budget_list = sorted(list(map(int, stdin.readline().rstrip().split())))
total_budget = int(stdin.readline().rstrip())

print(binary_search(budget_list, total_budget))

