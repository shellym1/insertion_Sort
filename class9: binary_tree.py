class Node:

    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None

def print_tree(root):
    if root is not None:
        print(root.value)
        print_tree(root.left)
        print_tree(root.right)


def search(root, data): #חיפוש איבר
    temp = root
    if data == root:
        return root
    while temp != None and temp.value != None:
        if data < temp.value:
            temp = temp.left
        else:
            temp = temp.right
    return temp

def find_minimum(root): #מינימום
    temp = root
    while temp.left != None:
        temp = temp.left
    return temp

def find_maximum(root): #מקסימום
    temp = root
    while temp.right != None:
        temp = temp.right
    return temp

def successor(root):
    temp = root
    if temp.right != None:
        find_minimum(temp)
    else:
        father = temp.parent
        while father != None and father.right == temp:
            father = father.paernt
            temp = temp.parent
    return father

def predeccessor(root):
    temp = root
    if temp.left != None:
        find_maximum(temp)
    else:
        father = temp.parent
        while father != None and father.left == temp:
            father = father.parent
            temp = temp.parent
    return father

def insert(root, data):
    new_node = Node(data)
    temp = root
    if temp == None:
        temp = new_node
    else:
        spy = None
        while temp != None:
            spy = temp
            if temp.value > data:
                temp = temp.left
            else:
                temp = temp.right
        if data < spy.value:
            spy.left = new_node
        else:
            spy.right = new_node
        new_node.parent = spy

def delete(root, v):
    temp = root
    if temp.right == temp.left == None:
        temp.parent = None
    else:
        if temp.left !=None:
            temp = temp.left
            temp.left.parent = temp.parent
            temp.parent = None
        if temp.right !=None:
            temp.right.parent = temp.parent





















#חיפוש איבר
def search(root, data):
    temp = root
    while temp != None and temp.value != data:
        if temp.value > data:
            temp = temp.left
        else:
            temp = temp.right
    return temp

#מציאת מקסימום
def find_maximum(root):
    temp = root
    while temp.left != None:
        temp = temp.left
    return temp

#מציאת מינימום
def find_minimum(root):
    temp = root
    while temp.right != None:
        temp = temp.right
    return temp

#מציאת מספר עוקב
def successor(root):
    v = root
    if v.right != None:
        return find_minimum(v.right)
    else:
        father = v.parent
        while father != None and father.right == v:
            father = father.parent
            v = v.parent
    return father

#מציאת עוקב של v משמאל
def predecessor(root):
    v = root
    if v.left != None:
        return find_minimum(v.left)
    else:
        father = v.parent
        while father != None and father.left == v:
            father = father.parent
            v = v.parent
    return father

#הכנסה
def insert(root, data):
    new_node = Node(data)
    if root == None:
        root = new_node
    else:
        temp = root
        spy = None
        while temp != None:
            spy = temp
            if temp.value > data:
                temp = temp.left
            else:
                temp = temp.right
    if data < spy.value:
        spy.left = new_node
    else:
        spy.right = new_node
    new_node = spy

#מחיקה
def delete(root):
    v = root
    father = v.parent
    if v == father.left:
        father.left = None
    else:
        father.right = None
    v.parent = None

    if v.left != None:
        x = v.left
        v.left = None
    else:
        x = v.right
        v.right = None

    if father.right == v:
        father.right = x
    else:
        father.left = x
    x.parent = father
    v.parent = None
#להסתכל על הקוד בדף האחרון של השיעור ולכתוב משם את מחיקה

def delete1(root, v):
    if v.left == None or v.right == None:
        y = v
    else:
        y = successor(v)

    if y.left != None:
        x = y.left
    else:
        x = y.right

    if x != None:
        x.parent = y.parent

    if y.parent == None:
        root = x
    else:
        if y == y.parent.left:
            y.parent,left = x
        else:
            y.parent.right = x

    if y != v:
        v.data = y.data

