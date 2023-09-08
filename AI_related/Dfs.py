from romanianmap import dict_gn

def takedata():
    startcity = input("enter the start city name ")
    goal =  input("enter the destination city name ")
    if startcity not in dict_gn.keys() or goal not in dict_gn.keys():
        print("invalid names for citys this are the citys \n ",dict_gn.keys())
        takedata()
    return startcity,goal

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
DFS("Arad","Bucharest",dict_gn)

