def insertion_Sort(A): #מיון הכנסה
    for i in range(len(A)):
        min_index = i
        for j in range(i, len(A)):
            if A[j] < A[min_index]:
                A[j], A[min_index] = A[min_index], A[j]
    return A

def insertionSort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j] < A[mini]:
                A[j], A[i] = A[i], A[j]
    return A






#מיון בועות מעביר את הגדול לסוף
def booble_Sort(A): #מיון בועות
    for i in range(len(A)):
        max_index = i
        for j in range(i, len(A)):
            if A[max_index] > A[j]:
                A[max_index], A[j] = A[j], A[max_index]
    return A

def booble_Sort2(A):
    for i in range(len(A)):
        maxi = i
        for j in range(i, len(A)):
            if A[maxi] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A



def selectionSort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[mini] > A[j]:
                mini = j
        A[i], A[mini] = A[mini], A[i]
    return A

# מיון בחירה
def selection_Sort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def selection_Sort2(A):
    B = []
    for i in range(len(A)):
        m = min(A)
        B.append(m)
        A.remove(m)
    return B

def selection_sort_rec(A, i):
    if i == len(A) -1:
        return A
    mini = i
    for j in range (i+1, len(A)): #find minimum
        if A[j] < A[mini]:
            mini = j
    A[mini], A[i] = A[i], A[mini] #swap
    return selection_sort_rec(A, i+1)


def main():
    print(insertion_Sort([5, 2, 4, 1, 6, 3]))
    print(insertionSort([5, 2, 4, 1, 6, 3]))
    print(booble_Sort([5, 2, 4, 1, 6, 3]))
    print(booble_Sort2([5, 2, 4, 1, 6, 3]))
    print(selectionSort([5, 2, 4, 1, 6, 3]))
    print(selection_Sort([5, 2, 4, 1, 6, 3]))
    print(selection_Sort2([5, 2, 4, 1, 6, 3]))
    a=[2,8,6,1,3,2,5]
    print(selection_sort_rec(a,0))


if __name__ == '__main__':
    main()


