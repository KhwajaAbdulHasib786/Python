class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DDL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        temp=self.start
        if temp!=None:
            while temp.next!=None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def Search(self,data):
        temp=self.start
        while temp!=None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next!=None:
                temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
    def delet_first(self):
        if self.start!=None:
            self.start=self.start.next
            if self.start!=None:
                self.start.prev=None
    def delet_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp!=None:
                temp=temp.next
            temp.prev.next=None
    def delet_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp!=None:
                if temp.item==data:
                    if temp.next!=None:
                        temp.next.prev=temp.prev
                    if temp.prev!=None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next




#driver mode:
mylist=DDL()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.Search(20),25)



mylist.print_list()
