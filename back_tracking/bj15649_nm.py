n, m = map(int, input().split())
ans = []
def back_track():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(1, n+1):
        print("i :", i)
        if i not in ans:
            print("before: ", ans)
            ans.append(i)
            print("mid :", ans)
            back_track()
            ans.pop()
            print("after :", ans)

back_track()