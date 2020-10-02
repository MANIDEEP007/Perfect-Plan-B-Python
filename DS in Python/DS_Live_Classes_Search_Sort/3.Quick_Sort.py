def partition(a,low,high):
    i = low - 1
    pivot = a[high]
    for j in range(low,high):
        if a[j] <= pivot:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[high] = a[high],a[i+1]
    return i+1
def quicksort(a,low,high):
    if low < high:
        pi = partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)
a = [10,7,8,9,1,5]
#Pass Array, Low and High Indexes
quicksort(a,0,len(a)-1)

#PrintSorted Array
for i in a:
    print(i)
