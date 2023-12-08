# djakstras also known as uniform cost search 
from romanianmap import dict_gn,dict_hn
from collections import deque
def djakstras(map,startcity,endcity):
    visited = []
    queue = deque()     
    queue.append(startcity)
    while queue:
        pointer = queue.popleft()
        visited.append(pointer)
        if pointer == endcity:
            return "ok got it"
        expands = dict_gn[pointer]
        print(pointer)
        min_key = None
        min_value = float('inf')
        for key,value in expands.items():
            if value < min_value:
                min_value = value
                min_key = key

        deque.append(min_key)
        
    return "fail"

out = djakstras(dict_gn,"Arad","Bucharest")
print(out)
