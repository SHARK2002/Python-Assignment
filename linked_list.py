
#Class node
from email import header
from platform import node


class Node:

    #parameterised function to initialize a node object
    def __init__(self,data):
        self.value=data
        self.next=None

#class linked list
class Linked_list:

    #function to initialize a linked list object
    def __init__(self):
        self.head=None;

    #function to append a node to a linked list
    def append (self,node):

        if(self.head==None):
            self.head=node
        
        else:
            temp = self.head

            while temp.next != None:
                temp=temp.next
            
            temp.next=node

    #function to prepend a node to a linkedlist
    def prepend (self,node):

        if(self.head==None):
            self.head=node

        else:
            node.next=self.head

            self.head=node

    #function to insert a node at the ith position
    def insert(self,node,index):
        if(self.head==None):
            self.head=node
        
        else:
            temp=self.head

            j=0

            while temp.next!=0 and j!=index-2:
                temp=temp.next
                
                j+=1

            ptr=temp.next

            temp.next=node
            node.next=ptr

    #function to print the linked list
    def print_list(self):

        temp=self.head


        while temp!=None:

            print(f"{temp.value} ->",end=" ")

        

        


        