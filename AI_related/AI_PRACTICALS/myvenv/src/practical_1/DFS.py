from romanianmap import dict_gn


def DFS(startcity,goal,map):
    printStack = []
    visited = {}
    visited[startcity] = None
    stack = []
    stack.append(startcity)
    while stack:
        
        current = stack.pop()
        print(current,'\n---------------------------------\n',stack,'\n-----------------------------\n')
        if current == goal:
            path = []
            while (current != None):
                path.append(current)
                current = visited[current]
            print("found\n" ,  path[::-1])

            return
        
        for i,j in map.get(current,{}).items():
            if i not in visited:
                stack.append(i)
                visited[i] = current
    return printStack
# if __name__ == '__main__':
# startcity,goal = takedata()
# ansBfs = BFS(startcity,goal,dict_gn)
# print(DFS("Arad","Bucharest",dict_gn))


def DFS_EASY(start,goal,map):
    stack = []
    stack.append(start)
    visited = set()
    while stack:
        print(stack)
        pointer = stack.pop()
        if pointer == goal:
            print("found goal city")
            return
        if pointer not in visited:
            visited.add(pointer)

            #expand the tree
            for i,j in map.get(pointer).items():
                stack.append(i)

print(DFS_EASY("Arad","Bucharest",dict_gn))

#if not romanian map defined explicitly 
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

def dfs(root, graph):
    if not root or root not in graph:
        return []

    result = []
    stack = [root]

    while stack:
        current_node = stack.pop()
        result.append(current_node)

        for child in reversed(graph[current_node]):
            stack.append(child)

    return result

# Perform DFS on the sample tree
# result = dfs("1", tree)
# print("DFS result:", result)
