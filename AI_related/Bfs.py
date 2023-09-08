
def BFS(startcity,goal,map):
    from collections import deque
    queue = deque() # a queue to push citys
    visited = {} # to keep track if visited?
    queue.append(startcity)
    visited[startcity] = None
    while queue: #run until queue is empty any value in queue is true

        lCity = queue.popleft() # pops left item and reurns a pointer 
        # print(lCity,"\n",queue,"\n") 
        if lCity == goal:
            print("found")
            p = []
            while lCity is not None:
                p.append(lCity)
                lCity = visited[lCity]

            return list(reversed(p))
        
        for i,j in map.get(lCity,{}).items(): # i is the child node of current node we will append them in the queue 
            if i not in visited:
                queue.append(i)
                visited[i] = lCity
                print(visited ,"\n")

    return [] # if no goal then return this

