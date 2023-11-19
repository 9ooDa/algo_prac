// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/77484#

def solution(lottos, win_nums):            
    count = 0
    zero_count = 0
    place = [6, 5, 4, 3, 2]
    
    for n in lottos:
        if n in win_nums:
            count += 1
        elif n == 0:
            zero_count += 1
        else:
            continue
            
    highest , lowest = 6, 6   
    if count + zero_count in place:
        highest = place.index(count + zero_count) + 1
    if count in place:
        lowest = place.index(count) + 1
    
    return [highest, lowest]
    
        