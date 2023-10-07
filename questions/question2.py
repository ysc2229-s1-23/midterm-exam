"""
Problem: Merge Two Sorted Lists

Description:
Given two sorted linked lists, merge them into a single sorted linked list. The list should be constructed by splicing the nodes from the two given lists together. Do not create new nodes.

Function Signature:
def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:

Inputs:
    - list1 (ListNode): Head of the first sorted linked list. Can be None.
    - list2 (ListNode): Head of the second sorted linked list. Can be None.

Returns:
    - ListNode: Head of the merged sorted linked list.

Examples:

1. 
    Input: 
        list1 = [1, 2, 4]
        list2 = [1, 3, 4]
    Output: 
        [1, 1, 2, 3, 4, 4]
    
    Explanation: 
        Both linked lists have sorted nodes. Splicing them together results in a merged sorted linked list.

2. 
    Input: 
        list1 = []
        list2 = []
    Output: 
        []
    
    Explanation: 
        Both lists are empty, so the merged list is also empty.

3. 
    Input: 
        list1 = []
        list2 = [0]
    Output: 
        [0]
    
    Explanation: 
        The first list is empty, so the merged list is just the second list.

Notes:
    - A simple two-pointer approach can be used. Traverse both lists, compare the current nodes' values, and add the smaller one to the result list.
    - The problem can also be approached recursively.

Tags:
    - Linked List
    - Two Pointers
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # Implementation here
    return ListNode()