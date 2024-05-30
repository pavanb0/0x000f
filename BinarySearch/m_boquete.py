arr = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3


def possible(arr,m,k,day):
    cnt = 0
    bqt = 0
    for i in range(len(arr)):
        if day>=arr[i]:
            cnt+=1
        else:
            bqt+=cnt//k
            cnt=0
    bqt += cnt//k
    return bqt>=m



def ans(arr,m,k):
    if m*k>len(arr):
        return -1
    minArr,maxArr = min(arr),max(arr)
    low,high = minArr,maxArr

    while low<=high:
        mid = (low+high)//2
        if (possible(arr,m,k,mid)):
            high = mid - 1
        else:
            low = mid + 1

    return low
        # high-=1



    # for i in range(min(arr),max(arr)):
    #     if possible(arr,m,k,i):
    #         return i
    # return -1


answer = ans(arr,m,k)
print(answer)