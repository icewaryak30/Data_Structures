#QUEUE IMPLEMENTATION USING LINKED LIST
class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
class Queue:
    def __init__(self):
            self.head=None
    def  display(self):
        temp=self.head
        if temp==None:
            print("No elements in the queue")
        else:
            while(temp!=None):
                print(temp.data,"==>",end="")
                temp=temp.next
            print("None")    
            
    def  Insertion(self,data):
        temp=Node(data)
        temp1=self.head
        if temp1==None:
            self.head=temp
        else:
            while(temp1.next!=None):
                temp1=temp1.next
            temp1.next=temp
        self.display()
    def Deletion(self):
        temp=self.head
        if temp==None:
            print("No elements in the queue")
        else:
            self.head=temp.next
            temp.next=None
            self.display()
obj=Queue()
opt=0
while opt<4:
    print("###QUEUE IMPLEMENTATION###")
    print("1.Insert to the queue 2.Delete from the queue 3.Display the queue")
    opt=int(input())
    if opt==1:
        print("Enter the element to be inserted")
        data=int(input())
        obj.Insertion(data)
    elif opt==2:
        obj.Deletion()
    elif opt==3:
        obj.display()
