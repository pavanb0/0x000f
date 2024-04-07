def mergeSort(arr: [int], l: int, r: int):
    # def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        R = arr[mid:]
        L = arr[:mid]
        mergeSort(L,0,0)
        mergeSort(R,0,0)

        i,j,k = 0,0,0
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1

    

