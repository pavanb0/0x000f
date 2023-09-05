from romanianmap import dict_gn
def takedata():
    startcity = input("enter the start city name ")
    goal =  input("enter the destination city name ")
    if startcity not in dict_gn.keys() or goal not in dict_gn.keys():
        print("invalid names for citys this are the citys \n ",dict_gn.keys())
        takedata()
    return startcity,goal


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


if __name__ == '__main__':
    startcity,goal = takedata()
    ans = BFS(startcity,goal,dict_gn)
    print(ans)
# print(dict_gn.keys())

"""
this is where we return the path this is the visited list look carefully 

see now we stat while leftnode not none
currently it will be the goal node 
so froom the dict below we take the goal node bucharest and from that its child which is fagarus 
then last node is renamed as fagarus 
we then go back till child is found as None
done return reversed version of it

{'Arad': None,
 'Zerind': 'Arad',
 'Timisoara': 'Arad',
 'Sibiu': 'Arad',
 'Oradea': 'Zerind',
 'Lugoj': 'Timisoara',
 'Rimnicu': 'Sibiu',
 'Fagaras': 'Sibiu',
 'Mehadia': 'Lugoj',
 'Pitesti': 'Rimnicu',
 'Craiova': 'Rimnicu',
 'Bucharest': 'Fagaras',
 'Drobeta': 'Mehadia'}

"""