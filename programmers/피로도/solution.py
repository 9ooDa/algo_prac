// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    # k - 소모 >= 다음 최소필요
    arr = list(permutations(dungeons))
    
    
    flag = 0
    for i in range(len(arr)):
        curr = k
        count = 0
        for j in range(len(dungeons)):
            if curr >= arr[i][j][0]:
                curr -= arr[i][j][1]
                count += 1
        if count > flag:
            flag = count
            
    return flag