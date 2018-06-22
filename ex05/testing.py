from singly_list import SinglyList
from node import Node
import random

disList = SinglyList()

for i in range(10):
    disList.add_head(Node(random.randint(1,100)))

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
disList.remove(disList.head, 4)
SinglyList.print_list(disList.head)

#03 Test
print(SinglyList.has_cycle(disList.head))

#04 Test
SinglyList.print_list(trainWon.head)
SinglyList.print_list(trainToo.head)
SinglyList.print_list(SinglyList.merge(trainWon.head, trainToo.head))
'''
#05 Test
SinglyList.print_list(disList.head)
disList.sort_asc(disList.head)
SinglyList.print_list(disList.head)
