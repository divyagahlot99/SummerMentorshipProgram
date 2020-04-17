class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push_start(self,new_data):
        new_data=Node(new_data)
        new_data.next=self.head
        self.head=new_node

def reverse(curr):
    new_curr=curr.next
    new_next=curr
    curr.next=None
    curr=new_curr
    while curr.next:
        new_curr=curr.next
        curr.next=new_next
        new_next=curr
        curr=new_curr
    curr.next=new_next
    return curr

def printlist(curr):
    while curr:
        print(curr.data)
        curr=curr.next


e1=Node('Mon')
e2=Node('Tue')
e3=Node('Wed')
e4=Node('Thur')
e5=Node('Fri')
e6=Node('Sat')
e7=Node('Sun')

e1.next=e2
e2.next=e3
e3.next=e4
e4.next=e5
e5.next=e6
e6.next=e7

printlist(reverse(e1))