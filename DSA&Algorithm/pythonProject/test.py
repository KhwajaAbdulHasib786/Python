class Node:
    def __init__(self,data,next):
        self.data= data
        self.next=  next
class linkedlist:
     def __init__(self):
         self.head = None
     def insert_at_begining(self,data):
         node =Node(data,self.head)
         self.head = node
     def print(self):
          itr =self.head
          llstr =''
          while itr:
              suffix = ''
              if itr.next:
                   suffix ='-->'
                   llstr+=str(itr.data)
              itr=itr.next
              print(llstr)
     def get_length(self):
         count = 0
         itr = self.head
         while itr:
             count+= 1
             itr=itr.next
             return count
     def inset_at_end(self,data):
         if self.head is None:
             self.head = Node(data,None)
             return
         itr = self.head
         while itr.next:
             itr = itr.next
         itr.next = Node(data)
     def inset_at(self,index,data):
         if index < 0 or index> self.get_length():
             raise Exception("Invalid Index")





if __name__== '__main__':
    root = linkedlist()
    root.inset_at_end(567)
    root.inset_at_end(99)


    root.print()
    print(root.get_length())




