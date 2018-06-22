from singly_list import SinglyList
from node import Node
import random

def main():
    trainWon = SinglyList()
    trainToo = SinglyList()

    for i in range(10):
        trainWon.add_head(Node(random.randint(1,100)))

    for i in range(10):
        trainToo.add_head(Node(random.randint(1,100)))

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

    #05 Test
    SinglyList.print_list(disList.head)
    disList.sort_dsc(disList.head)
    SinglyList.print_list(disList.head)
    '''
    #06 "Test"
    SinglyList.print_list(trainWon.head)
    SinglyList.print_list(trainToo.head)
    trainWon.sort_dsc(trainWon.head)
    trainToo.sort_dsc(trainToo.head)
    SinglyList.print_list(SinglyList.merge(trainWon.head, trainToo.head))

if __name__ == '__main__':
    main()
