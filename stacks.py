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

        for value in self.stack:
            print(value)




list=[1,2,3,4,5,6]

stack = Stack()

for item in list:

    stack.push(item)

stack.display()

print("<------------------------------->")

stack.pop()

stack.display()
print("<-------------------------------->")


