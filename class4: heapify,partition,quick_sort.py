def heapify(A, i, heap_size):
    left = 2*i + 1  # left index
    right = 2*i + 2  # right index

    maxi = i  # initialize

    if left < heap_size and A[maxi] < A[left]:  # if father < left
        maxi = left
    if right < heap_size and A[maxi] < A[right]:  # if ans < right
        maxi = right

    if maxi != i:  # if we need to swap
        A[i], A[maxi] = A[maxi], A[i]
        heapify(A, maxi, heap_size)

def build_heap(A):
    for i in range(int(len(A)/2), -1, -1):
        heapify(A, i, len(A))

def heap_sort(A):
    build_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)



#מימוש partition
def partition(A, left, right):
    left = A[0]
    right = len(A) -1
    pivot = A[right]
    while left < right:
        while A[left] < pivot and A[left] < len(A):
            left +=1
        while A[right] > pivot:
            right +=1
        if A[left] > A[right]:
            A[left], A[right] = A[right], A[left]
    return A

def quick_sort(A, l, r):
    while l < r:
        q = partition(A, l, r)
        quick_sort(A, l, q-1)
        quick_sort(A, q+1, r)
        return A







def main():
    A = [5,13,2,25,7,17,20,8,4]
    #A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    heap_sort(A)
    print(A)



    #partition(A, 0, 14)
    #print(A)

    #partition2(A, 0, 14)
    #print(A)


if __name__ == '__main__':
    main()
