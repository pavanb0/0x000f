# its just Astar without pathcost only manhatten distance 

from romanianmap import dict_hn,dict_gn
import heapq
import time
def greedy_best_first_search(start, goal, graph, heuristic):
    priority_queue = [(heuristic[start], start)]

    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        
        print(priority_queue)
        if current_node == goal:
            print("Found goal city")
            return

        for next_node, _ in graph.get(current_node).items():
            heapq.heappush(priority_queue, (heuristic[next_node], next_node))
          

greedy_best_first_search("Arad", "Bucharest", dict_gn, dict_hn)
