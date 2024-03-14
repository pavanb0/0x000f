def insertionSort(arr)->None:
    i = 0
    while i<= len(arr):
        for k in range(i,len(arr)):
            print(arr[k])
        print('\n')
        i+=1    
    
arr = [9, 13, 20, 24, 46, 52]
insertionSort(arr)
