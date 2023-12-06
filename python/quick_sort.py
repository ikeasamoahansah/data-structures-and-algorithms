
def sort(arr, start, end):
    if end<=start: 
        return
    pivot = partition(arr, start, end)

    sort(arr, start, pivot-1)
    sort(arr, pivot+1, end) 


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(end-1):
        if arr[j] < pivot:
            i+=1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        j+=1
    i+=1
    tmp = arr[i]
    arr[i] = arr[end]
    arr[end] = tmp
    return i

arr = [4, 7, 9, 3, 2, 5]
print(sort(arr, 0, len(arr)-1))