# bfs 버전 안됨
from collections import deque

def solution(tickets):
    dummy_tickets = tickets
    path = ["ICN"]
    queue = deque()
    
    # icn = []
    # for i in range(len(dummy_tickets)):
    #     if dummy_tickets[i][0] == "ICN":
    #         icn.append(dummy_tickets[i][1])
            
    # queue.append(("ICN", sorted(icn)[0]))
    # dummy_tickets.remove(queue[0])
    queue.append(("ICN", dummy_tickets[0][1]))
    
    
    while queue:
        depart, dest = queue.popleft()
        
        # print([depart, dest])

        for i in range(len(dummy_tickets)):
            next_depart = dummy_tickets[i][0]
            next_dest = dummy_tickets[i][1]

            if next_depart == dest:
                queue.append((next_depart, next_dest))
                path.append(next_depart)
                
        if len(dummy_tickets) == 1:
            path.append(dummy_tickets[0][1])
                
        dummy_tickets.remove([depart, dest])
        
        print(dummy_tickets)

    
    return path

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))