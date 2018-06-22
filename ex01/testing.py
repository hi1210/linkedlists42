from singly_list import SinglyList
from node import Node
from print_list import PrintList


disList = SinglyList()
for i in range(0):
    disList.add_head(Node(i))
'''
#00 Test
PrintList.print_list(disList.head)
disList.add_head(Node("lmao"))
PrintList.print_list(None)
PrintList.print_list(disList.head)
'''
#01 Test
PrintList.print_list(disList.head)
PrintList.add_tail(disList.head, 10)
PrintList.print_list(disList.head)
