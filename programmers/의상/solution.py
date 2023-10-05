// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42578#

from collections import defaultdict

def solution(clothes):
    all_clo = defaultdict(list)
    for i in range(len(clothes)):
        all_clo[clothes[i][1]] += [clothes[i][0]]
        
    count = 1
    for v in all_clo.values():
        count *= (len(v) + 1)
        
    return count - 1
        
    