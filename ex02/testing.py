from singly_list import SinglyList
from node import Node

disList = SinglyList()

disList.add_head(Node(4))
for i in range(1,10):
    disList.add_head(Node(i))

disList.add_head(Node(4))
disList.add_head(Node(5))
disList.add_head(Node(8))
disList.add_head(Node(4))
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
'''
#02 Test
SinglyList.print_list(disList.head)
disList.remove(disList.head, 4)
SinglyList.print_list(disList.head)
