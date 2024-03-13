import random
array = [random.randint(1,200) for _ in range(10)]
def maxInArray(arr):
    cur_max = [arr[0],0]
    for i in range(len(arr)):
        if cur_max[0] < arr[i]:
            cur_max = [arr[i],i]
        
    return cur_max
    
def sortArray(arr):#Selection Sort
    i = 0
    while i<len(arr):
        cur_min = i
        for k in range(i,len(arr)):
            if arr[k] < arr[cur_min]:
                cur_min = k
        # print('\n',cur_min,arr[cur_min]) 
        # print('\n')
        arr[i],arr[cur_min] = arr[cur_min],arr[i]
        i+=1

    return arr

print(array,'\n')
print(sortArray(array))
