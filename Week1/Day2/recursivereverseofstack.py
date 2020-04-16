from queue import LifoQueue
from queue import Queue

class Stack:
    def __init__(self, max_size=10):
        self.s=LifoQueue()
        self.s.currsize=0
        self.s.maxsize=max_size

    def size(self):
        return self.s.qsize()

    def push(self,elem):
        if self.s.currsize==self.s.maxsize:
            print("Stack is full!")
            return -1
        else:
            self.s.put(elem)
            self.s.currsize+=1

    def pop(self):
        if self.s.currsize==0:
            print("Stack is empty!")
            exit(0)
        else:
            self.s.currsize-=1
            elem=self.s.get()
            print("Element popped: ", elem)
            return elem

    def reverse(self):
        if not self.s.empty():
            temp=self.s.get()
            self.reverse()
            self.insert_below(temp)

    def insert_below(self, item):
        if self.s.empty():
            self.push(item)
        else:
            temp=self.s.get()
            self.insert_below(item)
            print("TEMP, ", temp)
            self.push(temp)

    def currsize(s):
        return self.s.currsize


    
def menu():
    print("MENU")
    print("1.Push")
    print("2.Pop")
    print("3.Reverse")
    print("4.Size")
    print("CHOOSE:", end=" ")
    opt=int(input())
    if opt>=1 and opt <=4:
        if opt==1:
            elem=int(input("Enter element: "))
            stack.push(elem)
        elif opt==2:
            stack.pop()
        elif opt==3:
            print(stack.reverse())
        else:
            print(stack.size())
        print("-----------------------------")
        menu()
    else:
        return


stack=Stack(50)
menu()




