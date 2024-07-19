'''
Sort a linked list of 0s, 1s and 2s
Last Updated : 20 Mar, 2023
Given a linked list of 0s, 1s and 2s, The task is to sort and print it.

Examples: 

Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL 
Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL

Input: 1 -> 1 -> 2 -> 1 -> 0 -> NULL 
Output: 0 -> 1 -> 1 -> 1 -> 2 -> NULL 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    count = [0, 0, 0]
    ptr = head
    while ptr is not None:
        count[ptr.data] += 1
        ptr = ptr.next
    i = 0
    ptr = head
    while ptr is not None:
        if count[i] == 0:
            i += 1
        else:
            ptr.data = i
            count[i] -= 1
            ptr = ptr.next
    return head

def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end = ' -> ')
        ptr = ptr.next
    print('NULL')
        