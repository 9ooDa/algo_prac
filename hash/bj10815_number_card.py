'''
통과
7분
'''
n = int(input())
num_card = list(map(int, input().split()))
m = int(input())
is_have = {k:0 for k in list(map(int, input().split()))}

for n in num_card:
    if n in is_have.keys():
        is_have[n] = 1

for n in is_have.values():
    print(n, end=' ')