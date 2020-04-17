import copy
from queue import LifoQueue

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
            return
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
            return elem

    def currsize(self,s):
        return self.s.currsize

    def sort(self):
        temps=LifoQueue()
        while not self.s.empty():
            print("INPUT")
            # self.s.printstack()
            print("\nTEMP")
            # printstack(temps)
            curr=self.s.get()
            print("\nCurr", curr)
            print("Temps", top(temps))
            print("Input", top(self.s))
            temps.put(curr)
            while top(temps)<top(self.s):
                elem=temps.get()
                self.s.put(elem)
            temps.put(curr)
        return temps

    def printstack(s): 
        t=""
        if s.size() == 0: 
            return
        x=top(s)
        t+=str(s.pop())+" "
        s.printstack()  
        s.push(x)
        print(t, end=" ")

# def top(s):
#     if s.qsize()!=0:
#         top_elem=s.pop()
#         s.push(top_elem)
#         return top_elem
#     else:
#         return -1
    def top(s):
        if s.qsize()!=0:
            top_elem=s.get()
            s.put(top_elem)
            return top_elem
        else:
            return -1

def top(s):
    if s.size()!=0:
        top_elem=s.pop()
        s.push(top_elem)
        return top_elem
    else:
        return -1

    
def menu():
    print("MENU")
    print("1.Push")
    print("2.Pop")
    print("3.SORT")
    print("4.Size")
    print("5.print")
    print("CHOOSE:", end=" ")
    opt=int(input())
    if opt>=1 and opt <=5:
        if opt==1:
            elem=int(input("Enter element: "))
            stack.push(elem)
        elif opt==2:
            stack.pop()
        elif opt==3:
            print(stack.sort())
        elif opt==4:
            print(stack.size())
        else:
            stack.printstack()
        print("-----------------------------")
        menu()
    else:
        return


stack=Stack(50)
menu()
