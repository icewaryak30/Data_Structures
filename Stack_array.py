#STACK IMPLEMENTATION
def push(list1,element):
    list1.insert(0,element)
    display(list1)
def pop(list1):
    if len(list1)==0:
        print("No element is present in the stack!!!")
    else:
        del(list1[0])
        display(list1)
def display(list1):
    if len(list1)==0:
        print("No element is present in the stack!!!")
    else:
        for i in range(len(list1)):
           
            print("|",list1[i],"|")
            print(" ___")
option=0
list1=[]
while option<=3:
    print("######STACK IMPLEMENTATION######")
    print("choose your operation")
    print("1.push in stack 2.pop from stack 3.dispaly stack")
    option= int(input())
    if option==1:
        print("enter the element to be pushed in stack")
        element=input()
        push(list1,element)
    elif option==2:
        pop(list1)
    elif option==3:
        display(list1)
