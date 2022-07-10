def merge_sort(A):
    if len(A) == 1:
        return A
    else:
            mid = len(A) // 2
            left = A[:mid]
            right = A[mid:]

            merge_sort(left)
            merge_sort(right)
            i=0
            j=0
            k=0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    A[k] = left[i]
                    i = i+1
                else:
                    A[k] = right[j]
                    j = j+1
                k = k+1
            while i < len(left):
                A[k] = left[i]
                i = i+1
                k = k+1
            while j < len(right):
                A[k] = right[j]
                j = j+1
                k = k+1
    return A

def merge(A):
    mid = A[len(A) // 2]
    left = A[:mid]
    right = A[mid:]

    merge(left)
    merge(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
    return A
























def main():
    A = [2, 3, 6, 1, 4, 5]
    B = [1]
    print(merge_sort(A))
    print(merge_sort(B))

if __name__ == '__main__':
    main()




