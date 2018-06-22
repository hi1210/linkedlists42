from singly_list import SinglyList
from node import Node

disList = SinglyList()
theFirstNode = Node("The First Node")
theLastNode = Node("The Last Node")

theLastNode.next = theFirstNode

disList.add_head(theLastNode)
for i in range(1,10):
    disList.add_head(Node(i))

disList.add_head(theFirstNode)
'''
#00 Test
PrintList.print_list(disList.head)
disList.add_head(Node("lmao"))
PrintList.print_list(None)
PrintList.print_list(disList.head)

#01 Test
PrintList.print_list(disList.head)
PrintList.add_tail(disList.head, 10)
PrintList.print_list(disList.head)

#02 Test
SinglyList.print_list(disList.head)
disList.remove([self], list_head=something, val=4)
disList.remove(4)
SinglyList.print_list(disList.head)
'''
#03 Test
print(SinglyList.has_cycle(disList.head))
