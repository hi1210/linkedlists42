from node import Node
from singly_list import SinglyList

class PrintList:

    def print_list(list_head):
        print("trying to print")
        while list_head:
            print(list_head.content)
            list_head = list_head.next
