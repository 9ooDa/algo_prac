// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42626#

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2:
        a = heapq.heappop(scoville)
        
        if a >= K:
            return count
        
        else:
            if len(scoville) >= 1:
                b = heapq.heappop(scoville)
                heapq.heappush(scoville, a + (b * 2))
                count += 1
            else:
                break
            
    if scoville[0] >= K:
        return count
    else:
        return -1