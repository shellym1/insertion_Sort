class Node:
    def __init__(self, data):
        self.value = data
        self.left= None
        self.right_sibling = None

def print_tree(root):
    if root is not None:
        print(root.value)
        print_tree(root.left)
        print_tree(root.right_sibling)

def hash_table(k_s_c):
    new_dict = {}
    for key in k_s_c:
        if k_s_c[key] in new_dict:
            new_dict[k_s_c[key]].append(key)
        else:
            new_dict[k_s_c[key]] = [key]

def binary_search(A, l, r, i):
    l = A[0]
    r = len(A) -1
    while l <= r:
        mid = len(A) // 2
        if i == A[mid]:
            return A[mid]
        elif i < A[mid]:
                return binary_search(A, l, mid-1, i)
        else:
            return binary_search(A, mid+1, r, i)








def main():
    '''
    V1 = Node(7)
    V2 = Node(10)
    V3 = Node(14)
    V4 = Node(40)
    V5 = Node(3)
    V6 = Node(70)
    V7 = Node(5)
    V8 = Node(17)
    V9 = Node(9)
    V10 = Node(16)

    V1.left = V2
    V1.right = V3
    V2.left = V4
    V3.left = V5
    V3.right = V6
    V5.left = V7
    V5.right = V8
    V6.right = V9
    V8.left = V10

    print_tree(V1)

    table = [[] for i in range(9)]
    my_input = [5,28,19,15,20,33,12,17,10]

    for i in my_input:
        table[i%9].append(i)

    for element in table:
        for sub_element in element:
            print(sub_element)

    print(table)
'''

    A = [1, 3, 5, 7, 10, 12, 15, 20, 30]
    x = 10
    binary_search(A, A[0], len(A), x)


if __name__ == '__main__':
    main()

