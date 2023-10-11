class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # Implementation here
    # return ListNode()
    dum = ListNode()
    tail = dum
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next 
        else:
            tail.next = list2
            list2 = list2.next 
        tail = tail.next 
    if list1:
        tail.next = list1 
    else:
        tail.next = list2 
    return dum.next 