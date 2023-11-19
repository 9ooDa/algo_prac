// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12930

import re

def solution(s):
    words = s.split(" ")
    print(words)
    new_w = ""
    w_li = []
    for w in words:
        if w == '':
            w_li.append('')
            continue
        for i in range(len(w)):
            if i % 2 != 0:
                new_w += w[i].lower()
            else:
                new_w += w[i].capitalize()
        w_li.append(new_w)
        new_w = ""
                
    return ' '.join(w_li)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     answer = ""
#     words = s.split(" ")    # .split()은 공백이 여러개일 때 전부 없애서 문제에 적합하지 않음
#     print(words)
#     new_word_list = []
#     if s.isspace():
#         return s
#     else:
#         for word in words:
#             print("word in loop: ", word)
#             new_word = ''
#             for i in range(len(word)):
#                 if i % 2 != 0:
#                     new_word += word[i].lower()
#                 else:
#                     new_word += word[i].upper()
#             new_word_list.append(new_word)
#         # answer = answer.replace(word, new_word)

#         return answer