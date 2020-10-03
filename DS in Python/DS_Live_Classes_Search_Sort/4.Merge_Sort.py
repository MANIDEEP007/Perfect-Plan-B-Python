def merge(a,low,mid,high):
    L = [0] * (mid-low+1)
    R = [0] * (high-mid)
    for i in range(0,mid-low+1):
        L[i] = a[low + i]
    for j in range(0,high-mid):
        R[j] = a[mid + j + 1]
    i = 0
    j = 0
    k = low
    while i < (mid-low+1) and j <(high-mid):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j+=1
        k += 1
    while i < (mid-low+1):
        a[k] = L[i]
        i+=1
        k+=1
    while j < (high-mid):
        a[k] = R[j]
        j+=1
        k+=1
def mergesort(a,low,high):
    if low < high:
        mid = (low+high) // 2
        mergesort(a,low,mid)
        mergesort(a,mid+1,high)
        merge(a,low,mid,high)
a = [10,7,8,9,1,5]
#Pass Array, Low and High Indexes
mergesort(a,0,len(a)-1)
#PrintSorted Array
for i in a:
    print(i)
