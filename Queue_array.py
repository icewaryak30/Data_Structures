#QUEUE IMPLEMENTATION
def insert1(list1,element):
    list1.append(element)
    display(list1)
def delete1(list1):
    if len(list1)==0:
        print("No elements in the queue!!!")
    else:
        del(list1[0])
        display(list1)
def display(list1):
    if len(list1)==0:
        print("No elements in the queue!!!")
    else:
        for i in range(len(list1)):
            print(list1[i],"==>",end="")
        print("None")
list1=[]
option=0
while option<=3:
    print("######QUEUE IMPLEMENTATION######")
    print("choose your operation")
    print("1.Insert into the queue 2.delete from queue 3.dispaly queue")
    option= int(input())
    if option==1:
        print("enter the element to be inserted into the queue")
        element=input()
        insert1(list1,element)
    elif option==2:
        delete1(list1)
    elif option==3:
        display(list1)
