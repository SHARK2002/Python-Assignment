"""
Stack Data Structure using Classes
"""

class Stack :

    def __init__(self):

        self.stack=[]
    

    def push(self,x):

        self.stack.append(x)

    def pop(self):

        self.stack.pop()

    def is_empty(self):

        if self.stack == []:
            return True
        else:
            return False


    def display(self):
        print("[",end=" ")
        for value in self.stack:
            print(value, sep=" ",end=" ")
        print("]")






