class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None
        self.hight = 1

def AVL_print_tree(root):
    if root is not None:
        print(root.value)
        AVL_print_tree(root.left)
        AVL_print_tree(root.right)

def in_order(root, value):
    temp = root.value
    while temp != None and temp.value != None:
        in_order(temp.left)
        print(temp.value)
        in_order(temp.right)

def pre_order(root, value):
    temp = root.value
    while temp != None and temp.value != None:
        print(temp.value)
        pre_order(temp.left)
        pre_order(temp.right)

def post_order(root, value):
    temp = root.value
    while temp != None and temp.value != None:
        post_order(temp.left)
        post_order(temp.right)
        print(temp.value)

def search(root, value):
    temp = root.value
    while temp is not None and temp.value is not None:
        if value == temp.value:
            return value
        else:
            if value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return value
    return "the value is not in the tree"

def left_rotation(self, x):
    y = x.right
    t = x.parent
    z = y.left
    #lets rotate:
    y.parent = t
    y.left = x
    x.parent = y
    x.right = z
    if z is not None:
        z.parent = x
    if t is not None:
        if t.left == x:
            t.left = y
        else:
            t.right = y
    else:
        self.root = y
    self.high_fix(x)

def right_rotation(self, x):
    y = x.left
    t = x.parent
    z = y.right
    #lets rotate:
    y.parent = t
    y.right = x
    x.parent = y
    x.right = z
    if z is not None:
        z.parent = x
    if t is not None:
        if t.left == x:
            t.left = y
        else:
            t.right = y
    else:
        self.root = y

def find_min(root, value):
    temp = root.value
    while temp is not None:
        temp = temp.left
    return temp

def find_max(root, value):
    temp = root.value
    while temp is not None:
        temp = temp.right
    return temp

def proccessor(v): #עוקב מימין
    temp = v.right.value
    if temp is not None:
        find_min(temp)
    else:
        father = temp.parent
        if father != None and father.right == temp:
            father = father.parent
            temp = temp.parent
    return father

def predecessor(v):
    temp = v.left.value
    if temp is not None:
        find_max(temp)
    else:
        father = temp.parent
        if father != None and father.left == temp:
            father = father.parent
            temp = temp.parent
    return father

def check_depth(root, hight): #בדיקת עומק של קודקוד
    temp = root.value
    while temp is not None:
        if temp.right != None:
            x = temp.right.hight
        else:
            x = 0
        if temp.left != None:
            y = temp.left.hight
        else:
            y = 0
        temp.hight = max(x, y) +1

def balance(root, hight):
    temp = root.value
    while temp is not None:
        check_depth(temp)
        if temp.hight >= 2:
            if temp.left.left != None:
                right_rotation(temp)
            else:
                left_rotation(temp)
                right_rotation(temp)
        elif temp.hight <= -2:
            if temp.right.right != None:
                left_rotation(temp)
            else:
                right_rotation(temp)
                left_rotation(temp)

def insert(root, value):
    temp = root.value
    new_node = Node(value)
    spy = 0
    if temp == None:
        temp = new_node
    while temp is not None:
        spy = temp
        if value > temp:
            temp = temp.right
        else:
            temp = temp.left
        if value > spy.value:
            spy.right = new_node
        else:
            spy.left = new_node
        new_node.parent = spy
    check_depth(new_node)
    balance(new_node)

def delete_node(root, v, data):
    temp = root.value
    if temp.right == None and temp.left == None:
        y = temp
    else:
        y = proccessor(temp)
        if y.right != None:
            x = y.right
        else:
            x = y.left
        if x is not None:
            x.parent = y
        else:
            t = y.parent
        if y.parent is not None:
            if y.parent.right == y:
                y.parent.right = x
            else:
                temp = x
        if y != temp:
            temp = y.value
        y.parent = y.right = y.left is None
        if t is not None:
            check_depth(t)
            balance(t)








def breath_first_search(g, s): #חיפוש לרוחב
    color = {}
    dist = {}
    father = {}

    for v in g:
        color[v] = 0
        dist[v] = -1
        father[v] = None

    queue = []

    color[s] = 1
    dist[s] = 0
    queue.append(s)

    while len(queue) > 0:
        v = queue.pop(0)
        for u in g[v]:
            if color[u] == 0:
                color[u] = 1
                dist[u] = dist[v] + 1
                father[u] = v
                queue.append(u)
        color[v] = 2
    print(color, dist, father)


def dfs(graph):
    global time
    # אתחול המילונים לצורך שמירת הפרמטרים עבור כל קודקוד
    n = len(graph)
    color = {k: 0 for k in graph}
    pi = {k: None for k in graph}
    begin = {k: None for k in graph}
    finish = {k: None for k in graph}


    for v in graph:
        if color[v] == 0:
            dfs_visit(graph, v, color, pi, begin, finish)

    return color, pi, begin, finish


def dfs_visit(graph, v, color, pi, begin, finish):

    global time

    color[v] = 1
    time += 1
    begin[v] = time

    for u in graph[v]:
        if color[u] == 0:
            pi[u] = v
            dfs_visit(graph, u, color, pi, begin, finish)

    time += 1
    finish[v] = time
    color[v] = 2


def dfs2(graph):
    global time
    n = len(graph)
    color = {k: 0 for k in graph}
    father = {k: None for k in graph}
    begin = {k: None for k in graph}
    finish = {k: None for k in graph}

    for v in graph:
        if v.color == 0:
            dfs

def dfs_visit(graph, v, color, pi, begin, finish):
    global time

    color[v] = 1
    time += 1
    begin[v] = time

    for u in v:
        if color[u] == 0:
            color = 1
            pi[u] = v
            dfs2(graph, u, color, pi, begin, finish)

    time += 1
    color[v] = 2
    finish[v] = time















def main():
    '''
    g = {"v1": ["v2", "v4"], "v2": ["v1", "v3"], "v3": ["v2"], "v4": ["v1", "v5", "v8"], "v5": ["v4", "v6", "v7", "v8"],
         "v6": ["v5", "v7"], "v7": ["v5", "v6", "v8"], "v8": ["v4", "v5", "v7"]}
    breath_first_search(g, 'v1')
    '''
    """
    1 --- 2     3 --- 4
    |     |  /  |  /  |
    |     |/    |/    |
    5     6 --- 7 --- 8
    """
    g = dict()
    g[1] = [2, 5]
    g[2] = [1, 6]
    g[3] = [4, 6, 7]
    g[4] = [3, 7, 8]
    g[5] = [1]
    g[6] = [2, 3, 7]
    g[7] = [3, 4, 7, 8]
    g[8] = [4, 7]
    c, p, b, f = dfs(g)
    print("color = ", c)
    print("pi = ", p)
    print("begin = ", b)
    print("finish = ", f)


if __name__ == '__main__':
    main()