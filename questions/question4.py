"""
Kth+2 Smallest Number in a Stream

Problem Statement:
Design a class that can efficiently find the Kth+2 smallest element in a stream of numbers.

Requirements:
1. The class should have a constructor which accepts an integer array containing initial numbers from the stream and an integer ‘K’.
2. The class should have a function add(int num) which will store the given number and return the Kth+2 smallest number.

Example:
Input: [8, 7, 6, 5, 4, 3, 2, 1], K = 2
1. Calling add(10) should return '4' (4th smallest).
2. Calling add(9) should return '5' (4th smallest).
3. Calling add(0) should still return '5' (4th smallest).

Note:
The stream can contain duplicate numbers.
Make sure to handle edge cases. When might we not be able to return the kth+2 smallest number?

Tags:
    - Sorting
    - Priority Queue
    - Google Interview Question

"""

import heapq

class KthPlusTwoSmallest:
    def __init__(self, nums, k):
        return

    def add(self, num):
        return -1
