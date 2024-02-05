def solution(A,B):
    answer = 0
    
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
#     while len(A) > 0:
#         a = min(A)
#         b = max(B)
#         answer += a * b
#         A.remove(a)
#         B.remove(b)
        
    return answer