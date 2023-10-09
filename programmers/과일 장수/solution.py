// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/135808#

def solution(k, m, score):
    score = sorted(score, reverse=True)
    res = 0
    
    for i in range(m-1, len(score), m):
        res += score[i] * m
        
    return res
        
    # score = sorted(score, reverse=True)
    # dummy = []
    # res = 0
    
#     for _ in range(len(score)):
#         if len(score) < m:
#             break
            
#         if len(dummy) < m:
#             dummy.extend(score[:m])
        
#         res += min(dummy) * m
#         dummy = []
#         score = score[m:]
            
    # return res