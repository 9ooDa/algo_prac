'''
통과
'''
# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# pokemon = {}
# for i in range(n):
#     pokemon[sys.stdin.readline().rstrip()] = i+1

# q = [sys.stdin.readline().rstrip() for _ in range(m)]

# for x in q:
#     if x.isdigit():
#         print(list(pokemon.keys())[list(pokemon.values()).index(int(x))])
#     else:
#         print(pokemon[x])
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
pokemon = {}
rev_pokemon = {}
for i in range(n):
    x = sys.stdin.readline().rstrip()
    pokemon[x] = i+1
    rev_pokemon[i+1] = x

for _ in range(m):
    x = sys.stdin.readline().rstrip()
    if x.isdigit():
        print(rev_pokemon[int(x)])
    else:
        print(pokemon[x])