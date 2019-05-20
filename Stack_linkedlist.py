#STACK IMPLEMENTATION USING LINKED LIST
class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
class Stack:
    def __init__(self):
            self.head=None
    def  display(self):
        temp=self.head
        if temp==None:
            print("No elements in the stack")
        else:
            while(temp!=None):
                print(temp.data,"==>",end="")
                temp=temp.next
            print("None")    
            
    def  Push(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
        self.display()
    def Pop(self):
        temp=self.head
        if temp==None:
            print("No elements in the stack")
        else:
            self.head=temp.next
            temp.next=None
            self.display()
obj=Stack()
opt=0
while opt<4:
    print("###STACK IMPLEMENTATION###")
    print("1.Push into the stack 2.Pop out from the stack 3.Display the stack")
    opt=int(input())
    if opt==1:
        print("Enter the element to be pushed")
        data=int(input())
        obj.Push(data)
    elif opt==2:
        obj.Pop()
    elif opt==3:
        obj.display()
