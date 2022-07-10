def left(i):
    return 2*i +1

def right(i):
    return 2*i + 2

def heapify(A, i):
    l = left(i)
    r = right(i)
    maxi = i

    # מוצאים איבר מקסימלי מבין האבא ו2 הבנים שלו
    if l < len(A) and A[l] > A[maxi]:
        maxi = l
    if r < len(A) and A[r] > A[maxi]:
        maxi = r

    # אם יש צורך בהחלפה
    if maxi != i:
        A[i], A[maxi] = A[maxi], A[i]
        heapify(A, maxi)












def build_heap(A):
    for i in range(len(A)//2 - 1, -1, -1):
        heapify(A, i)




def main():
    # Q1
    A = [27,17,3,16,13,10,1,5,7,12,4,8,9,0]
    heapify(A, 3)
    print(A)

    # Q2
    B = [4,1,3,2,16,9,10,14,8,7]
    build_heap(B)
    print(B)

    build_heap(A)
    print(A)

if __name__ == '__main__':
    main()