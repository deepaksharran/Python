class Node:
    def __init__(self,dataa):
        self.data=dataa
        self.nxt=None
class ll:
    def __init__(self):
        self.head=None
        
    def insertbeg(self,nd):
        nn=Node(nd)
        nn.nxt=self.head
        self.head=nn
        
    
    def insertatend(self,nd):
        nn=Node(nd)
        if self.head is None:
            self.head=nn
            return
        last=self.head
        while last.nxt:
            last=last.nxt
        last.nxt=nn
    
    def insertatmid(self,nd,mid):
        temp=self.head
        while temp is not None:
            if temp.data==mid:
                break
            temp=temp.nxt
        if temp is None:
            print("There is no such node")
        else:
            nn=Node(nd)
            nn.nxt=temp.nxt
            temp.nxt=nn
        
    def delatbeg(self):
        temp=self.head
        self.head=temp.nxt
        temp.nxt=None
        
    def delatend(self):
        tmp=self.head
        while tmp.nxt is not None:
            tmp=tmp.nxt
        tmp.data=None
        
    def delatmid(self,mid):
        temp=self.head
        while temp.nxt is not None:
            if temp.nxt.data==mid:
                break
            temp=temp.nxt
        if temp is None:
            print("There is no such node")
        else:
            temp.nxt=temp.nxt.nxt
        
    
    def display(self):
        temp=self.head
        while temp.nxt!=None:
            print(temp.data," ==> ",end='')
            temp=temp.nxt
        print(temp.data)   
        
llob=ll()
ch=0
print("LinkedList Implementation")
while ch<=5:
    print("1.Insert at begining     2.Insert at End     3.Insert at Middle     4.Delete at begining      5.Delete at end     6.Delete at middle     7.Display     8.Exit")
    ch=int(input())
    if ch==1:
        a=input("Enter a value : ")
        llob.insertbeg(a)
        llob.display()
    elif ch==2:
        a=input("Enter a value : ")
        llob.insertatend(a)
        llob.display()
    elif ch==3:
        a=input("Enter a new node : ")
        b=input("Enter the mid node: ")
        llob.insertatmid(a,b)
        llob.display()    
    elif ch==4:
        llob.delatbeg()
        llob.display()
    elif ch==8:
        llob.display()
        
    elif ch==5:
        llob.delatend()
        llob.display()
    elif ch==6:
        mid=input("Enter a node: ")
        llob.delatmid(mid)
        llob.display()
    else:
        llob.display()
