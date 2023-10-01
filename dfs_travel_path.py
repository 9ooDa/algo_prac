def solution(tickets):
    def dfs(i):
        visited[i] = 1
        depart = tickets[i][0]
        dest = tickets[i][1]
        path.append(dest)
        for j in range(len(tickets)):
            if dest == tickets[j][0] and visited[j] == 0:
                dfs(j)
        

    tickets = sorted(tickets, key=lambda x: x[1])
    visited = [0] * len(tickets)
    path = ["ICN"]
    
    
    for i in range(len(tickets)):
        if visited[i] == 0 and tickets[i][0] == "ICN":
            dfs(i)

    return path