// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12949

import numpy as np
def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    ans = np.ndarray.tolist(arr1 @ arr2)
    
    return ans
    