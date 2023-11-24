// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    s_list = s.split(" ")
    
    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()
    
    return ' '.join(s_list)
