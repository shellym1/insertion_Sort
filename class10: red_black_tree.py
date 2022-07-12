#בניית עץ אדום שחור, חיפוש הכנסה ומחיקה
#רשות: 41,38,31,12,19,8 לבצע הכנסה משמאל לימין
#בסוף כל הכנסה לסמן עלה שחור
#, , add_new

class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = None

def print_tree(root):
    if root is not None:
        print(root.value)
        print_tree(root.left)
        print_tree(root.right)

#חיפוש איבר
def search(root, data):
    temp = root
    if temp == None or temp.value == data:
        return root
    if root.value > data:
        search(root.left, data)
    else:
        search(root.right, data)

def find_minimum(root, value):
    temp = root.value
    while temp.left != None:
        temp = temp.left
    return temp

def find_maximum(root, value):
    temp = root.value
    while temp.right != None:
        temp = temp.right
    return temp

def preccessor(v):
    if v.right!= None:
        return find_minimum(v.right)
    else:
        father = v.parent
        while father != None and father.right == v:
            father = father.right
            v = v.parent
        return father

def predecessor(v):
    if v.left != None:
        return find_maximum(v.left)
    else:
        father = v.parent
        if father != None and father.left == v:
            father = father.left
            v = v.parent
        return father

def insert(root, data):
    new_node = Node(data)
    temp = root.value
    if temp.value == None:
        temp = new_node
    else:
        spy = None
        while temp.value != None:
            spy = temp
            if data < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        if data <spy.value:
            spy.left = new_node
        else:
            spy.right = new_node
        new_node.parent = spy


