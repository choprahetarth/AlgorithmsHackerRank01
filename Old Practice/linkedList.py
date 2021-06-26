# A simple python implementation of linked lists

# Node Class
class Node:
    # add an init function to start itself
    def __init__(self,data):
        self.data = data
        self.next = None # initialize the linked list with null pointer

# Linked List Class
class linkedList:
    # add an init function to initialize the head 
    def __init__(self):
        self.head = None # initialize the head of the LL

# function that traverses the linked list
def traverse(headValue):
    while(headValue!=None):
        print(headValue.data)
        headValue=headValue.next

# main function
if __name__ == '__main__':
    # pehle initialize the linked list
    linked_List = linkedList()
    # then assign the first node to the head value
    linked_List.head = Node(1)
    # then make two more nodes
    second = Node(2)
    third = Node(3)
    # then link the head's next value with the second node
    linked_List.head.next = second
    # then link the next of the second node with the third
    second.next = third
    # function to traverse a linked list 
    traverse(linked_List.head)

