#רשימה מקושרת חד כיוונית
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def print_list(self): #הדפסת הרשימה
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value): # הפונקציה מכניסה איבר חדש לתחילת הרשימה
        new_node = Node(value) #יצירת node חדש
        if self.head is None: #אם הרשימה ריקה
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def append(self, value): # פונקציה מכניסה איבר לסוף הרשימה
        new_node = Node(value)
        # אם הרשימה ריקה
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def insert(self, position, value): # הפונקציה מכניסה ערך לתוך מיקום (מתחילים מ1)
        new_node = Node(value)
        if position < 1: #אם המיקום קטן מ1 אז לא הגיוני
            print("ERROR -negative index")
        elif self.size < position - 1: #אם המיקום גדול מהגודל של הרשימה אז לא הגיוני
            print("ERROR - the list is too small")
        elif position == 1: #אם המיקום שווה 1 אז תכניס לראש הרשימה
            self.push(value)
        elif self.size == position - 1: #הכנסה לסוף הרשימה
            self.append(value)
        else: #הכנסה לאמצע הרשימה
            temp = self.head
            for i in range(1, position - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1

    def search(self, value, position):
        temp = self.value
        for i in range(0, position - 1):
            if self.head.value == value:
                self.head.value
            elif self.head.next:
                if self.head.value.next == value:
                    self.head.value.next

    def deleteFirst(self, value):
        temp = self.head
        if temp is None:
            return "ERROR- the list is empty"
        else:
            temp = temp.next
            self.head.next = None
            self.size -= 1

    def deletePosition(self, position):
        if self.head is None:
            return "ERROR- the list is empty"
        elif self.get_size() <  position:
            return "ERROR- out of range"
        elif position < 1:
            return "ERROR- position does not exist"
        elif position == 1:
            self.deleteFirst(position)
        else:
            temp = self.head
            while temp.next is not None:
                if temp.position == position:
                    temp.next.position = None
                else:
                    temp = temp.next
            self.size -= 1

#רשימה מקושרת דו כיוונית
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class   DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def push(self, value): # הפונקציה מכניסה איבר חדש לתחילת הרשימה
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.size += 1
        elif self.size > 0:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.size += 1

    def append(self, value):  # פונקציה מכניסה איבר לסוף הרשימה
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            self.size += 1

    def insert(self, position, value):  # הפונקציה מכניסה ערך לתוך מיקום (מתחילים מ1)
        new_node = Node(value)
        if position < 1:  # אם המיקום קטן מ1 אז לא הגיוני
            print("ERROR -negative index")
        elif self.size < position - 1:  # אם המיקום גדול מהגודל של הרשימה אז לא הגיוני
            print("ERROR - the list is too small")
        elif position == 1:  # אם המיקום שווה 1 אז תכניס לראש הרשימה
            self.push(value)
        elif self.size == position - 1:  # הכנסה לסוף הרשימה
            self.append(value)
        else:  # הכנסה לאמצע הרשימה
            temp = self.head
            for i in range(1, position - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1

    def deleteFirst(self, value):
        if self.size == 0:
            return "the list is empty"
        else:
            temp = self.head
            temp = temp.next
            self.head.next = None
            self.size -= 1

    def is_empty(self):
        if self.get_size == 0:
            return "the list is empty"

    def search(self, value, position):
        if self.head.value == value:
            return self.head
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.value == value:
                    return self.next
                else:
                    temp = temp.next

    def print_list(self):
        temp = self.head
        while temp.next is not None:
            print(temp.value)
            temp = temp.next





def main():
    # יצרנו רשימה
    my_linked_list = LinkedList()
    # יצרנו איברים
    fisrt = Node(10)
    secound = Node(20)
    third = Node(40)
    # הגדרנו את האיבר הראשון שיהיה ברשימה
    my_linked_list.head = fisrt
    my_linked_list.size += 1
    # יצרנו שרשרת
    my_linked_list.head.next = secound
    my_linked_list.head.next.next = third
    # הדפסת רשימה
    # my_linked_list.prink_list()
    # נכניס איבר להתחלה
    my_linked_list.append(10)
    my_linked_list.append(20)
    my_linked_list.append(40)

    my_linked_list.push(50)
    # my_linked_list.print_list()
    # נכניס איבר לסוף
    my_linked_list.append(60)
    # my_linked_list.print_list()

    # print("The size is : " my_linked_list.get.size())
    my_linked_list.insert(1, 700)

    # print("new_list:")
    my_linked_list.print_list()

    my_linked_list.deleteFirst(0)

if __name__ == '__main__':
    main()
