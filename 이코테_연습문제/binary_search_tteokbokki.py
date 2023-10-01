'''
(input)
4 6
19 15 10 17
'''
from sys import stdin
# 내 풀이
# def binary_search(arr, target, start, end):
#     while start <= end:
#         h = (start+end) // 2
        
#         remaining = sum([x - h if x > h else 0 for x in arr])
        
#         if remaining < target:
#             end = h - 1
#         else:
#             start = h + 1

#     return h

# 내 풀이랑 이론은 같음
def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start+end) // 2
        
        for x in arr:
            # 잘랐을 때 떡의 양 계산
            if x > mid:
                total += x - mid
        # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        if total < target:
            end = mid - 1
        # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이라 여기에서 result 기록
            start = mid + 1

    return result

n, m = map(int, stdin.readline().rstrip().split())
tteoks = sorted(list(map(int, stdin.readline().rstrip().split())))

ans = binary_search(tteoks, m, 0, max(tteoks))
print(ans)