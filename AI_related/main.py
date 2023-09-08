from romanianmap import dict_gn
from Bfs import BFS
from Dfs import DFS
def takedata():
    startcity = input("enter the start city name ")
    goal =  input("enter the destination city name ")
    if startcity not in dict_gn.keys() or goal not in dict_gn.keys():
        print("invalid names for citys this are the citys \n ",dict_gn.keys())
        takedata()
    return startcity,goal


if __name__ == '__main__':
    startcity,goal = takedata()
    # ansBfs = BFS(startcity,goal,dict_gn)
    ansDfs = DFS(startcity,goal,dict_gn)
    print(ansDfs)
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