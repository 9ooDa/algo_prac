// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12977#

# from itertools import combinations

def solution(nums):
    def is_prime(x):
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
        return prime
    
    ans = []
    res = []
    comb = []
    nums = sorted(nums)
    def back_track(start):
        if len(ans) == 3:
            comb.append(list(map(int, ans)))
            return
        
        for i in range(start, len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
                back_track(i + 1)
                ans.pop()
                
    back_track(0)
    
    # comb = list(combinations(nums, 3))
    count = 0
    for c in comb:
        num = sum(c)
        if is_prime(num):
            count += 1
            
    return count