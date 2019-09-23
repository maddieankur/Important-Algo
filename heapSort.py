def heapify(arr,n,i):
    largest = i
    childL = 2*i+1
    childR = 2*i+2
    if childL<n and arr[childL]>arr[largest]:
        largest = childL
    if childR<n and arr[childR]>arr[largest]:
        largest = childR
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)


"""
Algo:

1. Build Heap
2. Swap 0th and last element of unsorted array
    heapify for rebuild the heap structuress
"""
arr = [1,7,2,45,32,432]
heapsort(arr)
print(arr)
