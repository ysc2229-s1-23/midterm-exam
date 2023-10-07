from questions.question2 import merge_sorted_lists, ListNode
from random import randint

def test_merge_sorted_lists():

    # Helper function to convert list to ListNode
    def list_to_listnode(input_list):
        if not input_list:
            return None
        head = ListNode(input_list[0])
        current = head
        for val in input_list[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to compare two ListNodes
    def compare_listnodes(l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1, l2 = l1.next, l2.next
        return l1 is None and l2 is None

    # Test Case 1
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    expected = [1, 1, 2, 3, 4, 4]
    result = merge_sorted_lists(list_to_listnode(list1), list_to_listnode(list2))
    assert compare_listnodes(result, list_to_listnode(expected))

    # Test Case 2
    list1 = []
    list2 = []
    expected = []
    result = merge_sorted_lists(list_to_listnode(list1), list_to_listnode(list2))
    assert compare_listnodes(result, list_to_listnode(expected))

    # Test Case 3
    list1 = []
    list2 = [0]
    expected = [0]
    result = merge_sorted_lists(list_to_listnode(list1), list_to_listnode(list2))
    assert compare_listnodes(result, list_to_listnode(expected))

    # Test Case 4: Large Input
    list1 = sorted([randint(1, 1000) for _ in range(10000)])
    list2 = sorted([randint(1, 1000) for _ in range(10000)])
    expected = sorted(list1 + list2)
    result = merge_sorted_lists(list_to_listnode(list1), list_to_listnode(list2))
    assert compare_listnodes(result, list_to_listnode(expected))

    print("All tests passed!")

test_merge_sorted_lists()
