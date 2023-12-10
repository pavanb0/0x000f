# if explicite defined romanian map 
from collections import deque
from romanianmap import dict_gn
def BFS(startcity,goal,map): # with path print 
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
                # print(visited ,"\n")
    print(visited)
    return [] # if no goal then return this


def BFS_EASY(start,goal,map):
    queue = deque()
    queue.append(start)
    while queue:
        pointer = queue.popleft()
        print(queue)
        if pointer == goal:
            print("found")
            return 
        for i,j in map.get(pointer).items():
            queue.append(i)
    return []

path = BFS_EASY("Arad","Bucharest",dict_gn)
print(path)
# if not explicit defined romaninan map then
 
from collections import deque

tree = {
    "1": ["2", "3", "4"],
    "2": ["5", "6"],
    "4": ["7", "8"],
    "5": [],
    "6": [],
    "3": [],
    "7": [],
    "8": []
}

def bfs(root, graph):
    if not root or root not in graph:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        for child in graph[current_node]:
            queue.append(child)

    return result

# Perform BFS on the sample tree
result = bfs("1", tree)
print("BFS result:", result)