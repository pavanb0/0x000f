import random
random.seed(450)
arr = [random.randint(1,500) for _ in range(20)]

import heapq

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2 
        L = arr[:mid]
        mergeSort(L)
        R = arr[mid:]
        mergeSort(R)
        # print(L,'\n',R)
        # print(L)
        
    
    





def heapSort(arr)->list[int]:
    heapq.heapify(arr)
    ans = []
    while arr:
        ele = heapq.heappop(arr)
        ans.append(ele)
    return ans
ans = mergeSort(arr)
print(ans)
# ans1 = heapSort(arr)
# print(ans1)