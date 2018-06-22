from singly_list import SinglyList
from node import Node
from print_list import PrintList


disList = SinglyList()
for i in range(1,10):
    disList.add_head(Node(i))

PrintList.print_list(disList.head)
disList.add_head(Node("lmao"))
PrintList.print_list(None)
PrintList.print_list(disList.head)
