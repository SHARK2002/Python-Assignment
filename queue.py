"""
Queue Data Structures
"""


class Queue:
    
    def __init__(self):
        
        self.queue=[]

    def enque(self, x):
        
        self.queue.insert(0,x)

    def deque(self):

        if self.is_empty():
            print("Queue is Empty")
        else:
            self.queue.pop()
    
    def is_empty(self):

        if self.queue == []:
            return True
        else:
            return False

    def display(self):

        for values in self.queue:
            print(values)



