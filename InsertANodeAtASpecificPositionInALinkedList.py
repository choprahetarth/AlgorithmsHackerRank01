#!/bin/python3
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    global counter 
    counter = 0 
    nodeToBeShifted = head
    nodeBefore = head
    while(counter != position):
        counter+=1
        nodeToBeShifted = nodeToBeShifted.next
    counter=0
    while(counter!=(position-1)):
        counter+=1
        nodeBefore = nodeBefore.next
    print(nodeToBeShifted.data)
    print(nodeBefore.data)
    nodeToBeAdded = SinglyLinkedListNode(data)
    nodeBefore.next = nodeToBeAdded
    nodeToBeAdded.next = nodeToBeShifted
    return head



    

if __name__ == '__main__':