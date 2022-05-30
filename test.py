from stacks import Stack
from queue import Queue



print("This is a Stack")
list=[1,2,3,4,5,6]

stack = Stack()

for item in list:

    stack.push(item)

stack.display()

print("<------------------------------->")

stack.pop()

stack.display()
print("<-------------------------------->")

print("End of stack")



print("This is a Queue")

queue = Queue()

for item in list:

    queue.enque(item)

queue.display()

print("<------------------------------->")

queue.deque()

queue.display()
print("<-------------------------------->")

print("End of stack")

