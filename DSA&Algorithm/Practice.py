# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next
#
# class SSL:
#     def __init__(self,start=None):
#         self.start=start
#     def is_empty(self):
#         return self.start==None
#     def insert_at_first(self,data):
#         n=Node(data,self.start)
#         self.start=n
#     def insert_at_last(self,data):
#         n=Node(data)
#         if not self.is_empty():
#             temp=self.start
#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=n
#         else:
#             self.start=n
#     def Search(self,data):
#         temp=self.start
#         while temp is not None:
#             if temp.item==data:
#                 return temp
#             temp=temp.next
#         return None
#     def insert_after(self,temp,data):
#         if temp is not None:
#             n=Node(data,temp.next)
#             temp.next=n
#     def print_list(self):
#         temp=self.start
#         while temp is not None:
#             print(temp.item,end=" ")
#             temp=temp.next
#     def delet_first(self):
#         if self.start is not None:
#             self.start=self.start.next
#     def delet_last(self):
#         if self.start is None:
#             pass
#         elif self.start.next is None:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next is not None:
#                 temp=temp.next
#                 temp.next=None
#     def delet_item(self,data):
#         if self.start is None:
#             pass
#         elif self.start.next is None:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next is not None:
#                 if temp.next.item==data:
#                     temp.next=temp.next.next
#                     break
#                 temp=temp.next
#
#
#
#
#
# # driver Mode
# mylist=SSL()
# mylist.insert_at_first(10)
# mylist.insert_at_last(20)
# mylist.insert_at_last(30)
# mylist.insert_after(mylist.Search(20),25)
# mylist.insert_at_last(40)
# mylist.delet_item(40)
# mylist.delet_last()
# mylist.delet_first()
# mylist.print_list()