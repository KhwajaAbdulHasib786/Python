class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def Search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp!=None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item)
    def delet_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
    def delet_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
    def delet_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delet_first()
                else:
                    temp=self.last.next
                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:

                                self.delet_last()
                                break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break







mylist=CLL()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.Search(10),15)
mylist.delet_first()
mylist.delet_last()
mylist.delet_item(12)
mylist.print_list()