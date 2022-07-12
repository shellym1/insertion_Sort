def counting_sort(A):
    B = [0] * 10
    C = [0] * (len(A) + 1)

    for a in A:
        B[a % 10] += 1
    for i in range(1, len(B)):
        B[i] += B[i - 1]
    print(B)
    for a in A[::-1]:
        digit = a % 10
        C[B[digit]] = a
        B[digit] -= 1
    return C[1:]


#for radix: 

def counting_sort(A, j):
    B = [0]*10
    C = [0]*(len(A)+1)

    for a in A:
        B[(a//(10**j)) % 10] += 1
    for i in range(1, len(B)):
        B[i] = B[i] + B[i - 1]

    for a in A[::-1]:
        digit = (a//(10**j)) % 10
        C[B[digit]] = a
        B[digit] -= 1
    return C[1:]


def radix_sort(A, z):
    for i in range(z):
        A = counting_sort(A, i)
    return A






















'''
def main():
    A = [3,1,0,3,3]
    B = [329, 457, 657, 839, 436, 720, 355, 329, 457, 657, 839, 436, 720, 355,329, 457, 657, 839, 436, 720, 355]
#    counting_sort(A)

    radix_sort(B)
'''
def main():
    '''
    A = [329,457,657,839,436,720,355]
    print("original list: ", A)
    sorted_A = radix_sort(A, 3)
    print("sorted list: ", sorted_A)
'''
    #A = random_list.generate_list(4, 100, 999)
    A = [377, 504, 365, 305, 789, 107, 100, 276]
    print(A)
    print(radix_sort(A, 3))
    print(counting2(A))

if __name__ == '__main__':
    main()
