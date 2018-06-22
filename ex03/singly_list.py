class SinglyList(object):
    def __init__(self):
        self.h = None

    def __iter__(self):
        #in this context, head will be a Node
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def head(self):
        return self.h

    @head.setter
    def head(self, val):
        self.h = val

    def isEmpty(self):
        return self.head == None

    def add_head(self, node):
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    #prints a list item by item
    def print_list(list_head):
        print("trying to print")
        while list_head:
            print(list_head.content)
            list_head = list_head.next

    #adds an item to the end of a linked list
    def add_tail(list_head, val):
        if list_head == None:
            return
        while list_head.next:
            list_head = list_head.next
        list_head.next = Node(val)

    #removes an item from a list while keeping the list intact
    def remove(self, list_head = self.h, val):
        previous = None
        #if no list, ignore
        if list_head == None:
            return

        while list_head != None:
            if list_head.content == val:
                if previous == None:
                    self.h = list_head.next
                    list_head = self.h
                else:
                    previous.next = list_head.next
                    list_head = list_head.next
            else:
                previous = list_head
                list_head = list_head.next

    #check if a linked list is circular
    def has_cycle(list_head):
        if list_head == None:
            return False
        lastNode = list_head
        while lastNode.next != None:
            if lastNode.next == list_head:
                return True
            lastNode = lastNode.next
        return False
