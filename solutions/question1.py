# Python code to reverse a stack using queue
from collections import deque
 
def reverse_stack(stack):
    queue = deque()
     
    # Enqueue all into queue
    while stack != []:
        queue.append(stack.pop())
     
    # Now stack is empty thus  append all
    # elements back into the
    # stack - FIFO order
    while queue:
        stack.append(queue.popleft())
    return stack