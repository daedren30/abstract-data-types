# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:11:30 2021

@author: fb
"""

data = [1,2,3,4,5,6,7,8,9,10]
s = "---------------------------------"

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        curr = self.head
        while curr is not None:
           print(curr.value)
           curr = curr.next
            
    def insertHead(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        
    def insertTail(self, value):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        new = Node(value)
        curr.next = new
        
    def insertBetween(self, middle, value):
        if self.head == None:
            self.head = Node(value)
            return
        if middle == None:
            print("Node needed!")
            return
        new = Node(value)
        new.next = middle.next
        middle.next = new
        
def main():
    node1 = Node(25)
    node2 = Node(34)
    node3 = Node(57)
    node1.next = node2
    node2.next = node3
    
    list1 = LinkedList()
    list1.head = node1
    
    list1.printList()
    print(s)
    
    list1.insertHead('Head')
    list1.printList()
    print(s)
    
    list1.insertTail('Tail')
    list1.printList()
    print(s)
    
    list1.insertBetween(node2, 'Between')
    list1.printList()
    print(s)
    

if __name__ == "__main__":
    main()