"""
Problem: Reverse a Stack Using a Queue

Description:
A stack is a data structure that stores elements in a last-in-first-out (LIFO) order. A queue is another data structure that stores elements in a first-in-first-out (FIFO) order. Using the operations provided by a basic queue (enqueue, dequeue), your task is to reverse a given stack.

Function Signature:
def reverse_stack(stack: List[int]) -> List[int]:

Inputs:
- stack (List[int]): A list of integers representing the stack. The top of the stack is the last element of the list.

Returns:
- List[int]: The reversed stack. 

Examples:

1. 
Input: 
stack = [1, 2, 3, 4, 5]
Output: 
[5, 4, 3, 2, 1]
Explanation:
The top of the original stack is 5. After reversing, the top becomes 1.

2. 
Input: 
stack = [10, 20, 30]
Output: 
[30, 20, 10]
Explanation:
The original stack has 30 at the top. After reversing, 10 is at the top.

3. 
Input:
stack = [7]
Output:
[7]
Explanation:
A stack with a single element remains unchanged when reversed.

Notes:
- Do not use any additional data structures other than the queue provided.
- Consider the basic operations provided by a queue: enqueue (to insert an item) and dequeue (to remove an item).
- Think about how you can utilize these operations to help reverse the stack.
- Although this problem can be solved without using a queue, you will get no credits for the problem if you do not use a queue.
- Please reverse the stack in-place. Do not create a new stack.

Tags:
- Stack
- Queue
- Data Structures
"""

from collections import deque
from typing import List

def reverse_stack(stack: List[int]) -> List[int]:
    # Your implementation here
    pass
