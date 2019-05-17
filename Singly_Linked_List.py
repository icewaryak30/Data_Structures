class Node:
      def __init__(self,data):
            self.data=data
            self.next=None
class Singly_Linked_List:
      def __init__(self):
            self.head=None
      def  display(self):
            temp=self.head
            while(temp!=None):
                  print(temp.data,"==>",end="")
                  temp=temp.next
            print("None")    
            
      def  Insertion_at_begining(self,data):
            temp=Node(data)
            temp.next=self.head
            self.head=temp
      def  Insertion_at_middle(self,data,pos):
            temp=Node(data)
            temp1=self.head
            if temp1==None :
                  self.Insertion_at_begining(data)
            else:
                  c=1
                  while(c!=pos-1):
                        temp1=temp1.next
                        c+=1
                  temp.next=temp1.next
                  temp1.next=temp
                  
            
      def  Insertion_at_end(self,data):
            temp=Node(data)
            temp1=self.head
            while(temp1.next!=None):
                  temp1=temp1.next
            temp1.next=temp
      def Deletion_at_begining(self):
            temp=self.head
            if temp==None:
                  print("invalid")
            else:
                  self.head=temp.next
                  temp.next=None
                  self.display()
      def Deletion_at_middle(self,pos):
            temp1=self.head
            c=1
            while(c!=pos-1):
                  temp1=temp1.next
                  c+=1
            temp=temp1.next
            temp1.next=temp.next
            temp.next=None
           
              
             
      def Deletion_at_end(self):
            temp=self.head
            temp1=temp.next
            while(temp1.next!=None):
                  temp1=temp1.next
                  temp.next=temp1
            temp.next=None
            self.display()
             
obj=Singly_Linked_List()                  
ch=0
while(ch!=8):
      print('1.Insertion at begining','2.Insertion at Middle','3.Insertion at end','4.Deletion at begining','5.Deletion at Middle','6.Deletion at end',"7.Dislpay",'8.exit')
      ch=int(input())
      if(ch==1):
            print("enter the Node to be inserted at begining")
            data=input()
            obj.Insertion_at_begining(data)
            obj.display()
      if(ch==2):
            print("enter node to be inserted at middle")
            data=input()
            print("enter the position")
            pos=int(input())
            obj.Insertion_at_middle(data,pos)
            obj.display()
      if(ch==3):
            print("enter node to be inserted at end")
            data=input()
            obj.Insertion_at_end(data)
            obj.display()
      if(ch==4):
            obj.Deletion_at_begining()
      if(ch==5):
            print("enter the position")
            pos=int(input())
            obj.Deletion_at_middle(pos)
            obj.display()
      if(ch==6):
            obj.Deletion_at_end()
            
      if(ch==7) :
            obj.display()
             
            
            
            
            
      
