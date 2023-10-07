"""
Problem: Find the Second Next Letter

Description:
Given an array of lowercase letters sorted in ascending order, determine the second smallest letter in the given array greater than a specified 'key'. Assume the array is a circular list, which means that the last letter is assumed to be connected with the first letter. This implies that the smallest letter in the array is greater than the last letter of the array and is also the first letter of the array. Write a function to return the second next letter of the given 'key'.

Function Signature:
def find_second_next_letter(letters: List[str], key: str) -> str:

Inputs:
    - letters (List[str]): A list of lowercase letters sorted in ascending order. 
    - key (str): A single lowercase letter for which we need to find the second next letter in the array.

Returns:
    - str: The second next letter of the specified 'key' from the given list.

Examples:
1. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'f'
   Output: 'a'
   Explanation: The second smallest letter greater than 'f' is 'a' in the given array.

2. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'b'
   Output: 'f'
   Explanation: The second smallest letter greater than 'b' is 'f'.

3. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'm'
   Output: 'c'
   Explanation: As the array is assumed to be circular, the second smallest letter greater than 'm' is 'c'.

4. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'h'
   Output: 'c'
   Explanation: As the array is assumed to be circular, the second smallest letter greater than 'h' is 'c'.

Notes:
    - Binary Search can be utilized to solve the problem efficiently due to the sorted nature of the list.

Tags:
    - Binary Search
    - Arrays
"""
from typing import List

def find_second_next_letter(letters, key):
    return ""